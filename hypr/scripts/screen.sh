#!/bin/bash

mode_options=("Auto" "Single Display" "Multiple Displays" "Mirror" "Manage")

output=$(hyprctl monitors)
monitor_names=($(echo "$output" | grep -oP 'Monitor \K[^ ]+'))

mode=$(printf '%s\n' "${mode_options[@]}" | rofi -dmenu -p "Select Mode:")

if [ "$mode" == "${mode_options[0]}" ]; then
    hyprctl reload

elif [ "$mode" == "${mode_options[1]}" ]; then
    selected_monitor=$(printf "%s\n" "${monitor_names[@]}" | rofi -dmenu -i -p "Select Monitor: ")

    # delete chosen Display from array
    for (( i=0; i<${#monitor_names[@]}; i++ )); do 
        if [ "${monitor_names[i]}" == "$selected_monitor" ]; then
            monitor_names=( "${monitor_names[@]:0:$i}" "${monitor_names[@]:$((i + 1))}" )
            i=$((i - 1))
        fi
    done

    hyprctl keyword monitor "${monitor_names[0]}",disable

elif [ "$mode" == "${mode_options[2]}" ]; then 

    hyprctl reload
    selected_monitor=$(printf "%s\n" "${monitor_names[@]}" | rofi -dmenu -i -p "Main Monitor: ")

    for i in $(seq 1 5); do
        hyprctl dispatch moveworkspacetomonitor "$i" "$selected_monitor"
    done

    # delete chosen Display from array
    for (( i=0; i<${#monitor_names[@]}; i++ )); do 
        if [ "${monitor_names[i]}" == "$selected_monitor" ]; then
            monitor_names=( "${monitor_names[@]:0:$i}" "${monitor_names[@]:$((i + 1))}" )
            i=$((i - 1))
        fi
    done

    for i in $(seq 6 10); do
        hyprctl dispatch moveworkspacetomonitor "$i" "${monitor_names[0]}"
    done

elif [ "$mode" == "${mode_options[3]}" ]; then
    selected_main=$(printf "%s\n" "${monitor_names[@]}" | rofi -dmenu -i -p "Select Monitor: ")
    selected_mirror=$(printf "%s\n" "${monitor_names[@]}" | rofi -dmenu -i -p "Select Monitor to Mirror: ")
    echo $selected_main
    echo $selected_mirror
    hyprctl keyword monitor $selected_main,prefered,auto,1,mirror,$selected_mirror

elif [ "$mode" == "${mode_options[4]}" ]; then
    wdisplays
fi

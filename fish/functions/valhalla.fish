function valhalla
    set -l primary 8 secondary 9
    if test (count $argv) -eq 2
        set primary $argv[1]
        set secondary $argv[2]
    end

    set -l mon1 "DP-$primary"
    set -l mon2 "DP-$secondary"

    killall waybar
    hyprctl reload
    hyprctl keyword monitor DP-$primary,preferred,auto,2.0
    hyprctl keyword monitor DP-$secondary,preferred,auto,2.0

    for ws in (seq 1 5)
        hyprctl dispatch moveworkspacetomonitor $ws $mon1
        hyprctl keyword workspace $ws,monitor:$mon1
    end

    for ws in (seq 6 9)
        hyprctl dispatch moveworkspacetomonitor $ws $mon2
        hyprctl keyword workspace $ws,monitor:$mon2
    end

    hyprctl keyword monitor eDP-1,disable
    waybar &> /dev/null & disown
end

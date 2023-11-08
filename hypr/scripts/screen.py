#!/usr/bin/env python3

import subprocess
import re

def run_command(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8').strip()

def rofi_prompt(options, prompt):
    cmd = 'echo -e "{}" | rofi -dmenu -i -p "{}"'.format('\n'.join(options), prompt)
    return run_command(cmd)

def get_monitor_names():
    output = run_command("hyprctl monitors")
    return [line.split()[1] for line in output.splitlines() if "Monitor" in line]

def get_monitor_resolutions():
    output = run_command("hyprctl monitors")
    resolutions = re.findall(r'(\d+x\d+)@\d+\.\d+', output)
    return resolutions

def extract_dimensions(res_string):
    match = re.match(r'(\d+)x(\d+)', res_string)
    if match:
        return [int(match.group(1)), int(match.group(2))]
    return []

def auto_mode():
    run_command("hyprctl reload")

def move_workspace_to_monitor(workspaces : list, monitor : str):
    for workspace in workspaces:
        run_command(f'hyprctl dispatch moveworkspacetomonitor {workspace} {monitor}')

def split_workspaces_to_monitors(main_monitor : str, monitors : list):
        # move workspaces to first monitor
        selected_monitor = main_monitor 
        workspaces = ["1", "2", "3", "4", "5"]
        move_workspace_to_monitor(workspaces, selected_monitor)

        # move workspaces to second monitor
        if selected_monitor in monitors:
            monitors.remove(selected_monitor)
        workspaces = ["6", "7", "8", "9", "10"]
        move_workspace_to_monitor(workspaces, monitors[0])


def single_display_mode(monitor_names):
    selected_monitor = rofi_prompt(monitor_names, "Select Monitor:")

    if selected_monitor in monitor_names:
        monitor_names.remove(selected_monitor)

    if selected_monitor in ["DP-4", "DP-5"]:
        run_command(f'hyprctl keyword monitor {monitor_names[0]},disable')
        run_command(f'hyprctl keyword monitor {selected_monitor},2560x1440,0x0,1')
    else:
        run_command(f'hyprctl keyword monitor {monitor_names[0]},disable')
        run_command(f'hyprctl keyword monitor {selected_monitor},prefered,0x0,1')

def multiple_displays_mode(monitor_names):
    
    conifiguration = rofi_prompt(["default", "manual"], "Select Configuration:")

    if conifiguration == "default":
        split_workspaces_to_monitors("eDP-1", monitor_names[:])
        
    if conifiguration == "manual":
        # select main monitor
        selected_monitor = rofi_prompt(monitor_names, "Main Monitor:")
        selected_position = rofi_prompt(["side by side","stacked"], "Position:")
        selected_monitor_index = monitor_names.index(selected_monitor)
        resolutions = get_monitor_resolutions()
        selected_monitor_resolution = resolutions[selected_monitor_index]

        # remove selected monitor and resolution from lists 
        if selected_monitor in monitor_names:
            monitor_names.remove(selected_monitor)
        if selected_monitor_resolution in resolutions:
            resolutions.remove(selected_monitor_resolution)

        # set position 
        if selected_position == "side by side":
            dimensions = extract_dimensions(selected_monitor_resolution)
            position = f'{dimensions[0]}x0'
            run_command(f'hyprctl keyword monitor {selected_monitor},{selected_monitor_resolution},0x0,1')
            run_command(f'hyprctl keyword monitor {monitor_names[0]},{resolutions[0]},{position},1')
        if selected_position == "stacked":
            dimensions = extract_dimensions(resolutions[0])
            position = f'0x{dimensions[1]}'
            print(position)
            run_command(f'hyprctl keyword monitor {monitor_names[0]},{resolutions[0]},0x0,1')
            run_command(f'hyprctl keyword monitor {selected_monitor},{selected_monitor_resolution},{position},1')

        split_workspaces_to_monitors(selected_monitor, monitor_names[:])

def mirror_mode(monitor_names):
    selected_main = rofi_prompt(monitor_names, "Select Monitor:")
    selected_mirror = rofi_prompt(monitor_names, "Select Monitor to Mirror:")
    run_command(f'hyprctl keyword monitor {selected_main},prefered,auto,1,mirror,{selected_mirror}')

def manage_mode():
    run_command("wdisplays")

def main():
    mode_options = ["Auto", "Single Display", "Multiple Displays", "Mirror", "Manage"]
    monitor_names = get_monitor_names()

    # Run again if one monitor is deactived
    if len(monitor_names) < 2:
        auto_mode()
        monitor_names = get_monitor_names()

    mode = rofi_prompt(mode_options, "Select Mode:")

    if mode == "Auto":
        auto_mode()
    elif mode == "Single Display":
        single_display_mode(monitor_names)
    elif mode == "Multiple Displays":
        multiple_displays_mode(monitor_names)
    elif mode == "Mirror":
        mirror_mode(monitor_names)
    elif mode == "Manage":
        manage_mode()
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()


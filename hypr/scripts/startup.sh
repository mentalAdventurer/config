#!/usr/bin/bash

#######################################################################
#                         Startup Application                         #
#######################################################################

dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
pgrep nm-applet > /dev/null || nm-applet --indicator &
pgrep blueman-applet > /dev/null || blueman-applet &

#pgrep wluma > /dev/null && killall wluma
#wluma &

killall wl-paste 
wl-paste --watch cliphist store &

pgrep batsignal > /dev/null || batsignal -w 25 -c 10 -d 5 &
pgrep dunst > /dev/null || dunst &

pgrep -f polkit-kde-authentication-agent-1 > /dev/null ||
    /usr/lib/x86_64-linux-gnu/libexec/polkit-kde-authentication-agent-1 &

pgrep gnome-keyring-d > /dev/null ||
    /usr/bin/gnome-keyring-daemon --start --components=ssh,secrets,pkcs11 &

pgrep hypridle > /dev/null ||
    hypridle &

# swayosd
#pgrep swayosd-server > /dev/null ||
#    swayosd-server &

# Waybar
pgrep waybar > /dev/null || waybar &
pgrep hyprland-autoname-workspaces > /dev/null || hyprland-autoname-workspaces &

# Load Wallpaper
pgrep hyprpaper > /dev/null || hyprpaper &

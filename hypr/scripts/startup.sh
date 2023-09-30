#!/usr/bin/bash

#######################################################################
#                         Startup Application                         #
#######################################################################

dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
pgrep nm-applet > /dev/null || nm-applet --indicator &
pgrep blueman-applet > /dev/null || blueman-applet &

pgrep wluma > /dev/null && killall wluma
wluma &

killall wl-paste 
wl-paste -t text --watch clipman store --max-items=6000 --no-persist &
wl-paste -p -t text --watch clipman store --max-items=6000 -P --histpath="~/.local/share/clipman-primary.json" &
pgrep batsignal > /dev/null || batsignal -w 25 -c 10 -d 5 &
pgrep swaync > /dev/null || swaync & 

pgrep kdeconnectd > /dev/null || 
    /usr/lib/kdeconnectd &

pgrep polkit-kde-auth > /dev/null || 
    /usr/lib/polkit-kde-authentication-agent-1 &

pgrep gnome-keyring-d > /dev/null ||
    /usr/bin/gnome-keyring-daemon --start --components=ssh,secrets,pkcs11 &

pgrep swayidle > /dev/null || 
    ~/.config/hypr/scripts/swayidle.sh &

#pgrep event_handler.sh > /dev/null || 
#    ~/.config/hypr/scripts/event_handler.sh &

# swayosd
pgrep swayosd-server > /dev/null || 
    swayosd-server &

# Waybar
pgrep waybar > /dev/null || waybar &
pgrep hyprland-autoname-workspaces > /dev/null || hyprland-autoname-workspaces &

# Load Wallpaper
pgrep swww-daemon > /dev/null || swww init 
sleep 1 && wallpaper load

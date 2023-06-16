#!/usr/bin/bash

#######################################################################
#                             ENVIRONMENT                             #
#######################################################################

if [ ! -v wrapperhl ]; then 
    export PATH=$PATH:/home/fabian/.local/bin
    export XDG_CONFIG_HOME=$HOME/.config
    export XDG_CACHE_HOME=$HOME/.cache
    export XDG_DATA_HOME=$HOME/.local/share
    export ZDOTDIR=$HOME/.config/zsh
    export _JAVA_AWT_WM_NONREPARENTING=1
    export XCURSOR_SIZE=24
fi

#######################################################################
#                         Startup Application                         #
#######################################################################

dbus-update-activation-environment --systemd WAYLAND_DISPLAY XDG_CURRENT_DESKTOP
pgrep nm-applet > /dev/null || nm-applet --indicator &
pgrep blueman-applet > /dev/null || blueman-applet &

pgrep clight > /dev/null && killall clight
clight &

killall wl-paste 
wl-paste -t text --watch clipman store --max-items=6000 --no-persist &
wl-paste -p -t text --watch clipman store --max-items=6000 -P --histpath="~/.local/share/clipman-primary.json" &
pgrep batsignal > /dev/null || batsignal -w 25 -c 10 -d 5 &
pgrep dunst > /dev/null || dunst & 

pgrep polkit-kde-auth > /dev/null || 
    /usr/lib/polkit-kde-authentication-agent-1 &

pgrep gnome-keyring-d > /dev/null ||
    /usr/bin/gnome-keyring-daemon --start --components=ssh,secrets,pkcs11 &

pgrep swayidle > /dev/null || 
    ~/.config/hypr/scripts/swayidle.sh &

# Waybar
pgrep waybar > /dev/null || waybar &
pgrep hyprland-autoname-workspaces > /dev/null || hyprland-autoname-workspaces &

# Load Wallpaper
pgrep swww-daemon > /dev/null || swww init 
sleep 1 && wallpaper load

#!/usr/bin/bash

#######################################################################
#                             ENVIRONMENT                             #
#######################################################################

if [ ! -v wrapperhl ]; then 
    export PATH=$PATH:/home/fabian/.local/bin
    export XDG_CONFIG_HOME=$HOME/.config
    export XDG_CACHE_HOME=$HOME/.cache
    export XDG_DATA_HOME=$HOME/.local/share
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

#pgrep kdeconnectd > /dev/null ||
#    /usr/lib/kdeconnectd &

#pgrep kdeconnect-indicator > /dev/null ||
#    kdeconnect-indicator &

pgrep swayidle > /dev/null || 
    swayidle -w timeout 120 'hyprctl dispatch dpms off' \
                resume 'hyprctl dispatch dpms on' \
                timeout 180 'hyprctl dispatch dpms on && /home/fabian/.config/hypr/scripts/lock & sleep 2 && hyprctl dispatch dpms off' \
                resume 'hyprctl dispatch dpms on' \
                timeout 10 'if pgrep -x swaylock; then hyprctl dispatch dpms off; fi' \
                resume 'hyprctl dispatch dpms on' &
pgrep waybar > /dev/null || waybar &

# Load Wallpaper
pgrep swww-daemon > /dev/null || swww init 
wallpaper load

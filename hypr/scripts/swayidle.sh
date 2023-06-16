#!/usr/bin/bash

swayidle -w timeout 180 'hyprctl dispatch dpms off' \
        resume 'hyprctl dispatch dpms on' \
        timeout 240 'hyprctl dispatch dpms on && /home/fabian/.config/hypr/scripts/lock & sleep 2 && hyprctl dispatch dpms off' \
        resume 'hyprctl dispatch dpms on' \
        timeout 10 'if pgrep -x swaylock; then hyprctl dispatch dpms off; fi' \
        resume 'hyprctl dispatch dpms on' \
        timeout 1800 'hyprctl dispatch dpms on && sleep 2 && systemctl suspend' &

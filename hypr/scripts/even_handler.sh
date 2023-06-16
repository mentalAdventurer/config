#!/usr/bin/bash

# Event Handler

screencast() {
    state=$(echo "$1" | rg -o "([0-9]+)" | head -1)

    if [ "$state" -eq 1 ]; then
        pgrep swayidle > /dev/null && killall swayidle
    elif [ "$state" -eq 0 ]; then
        pgrep swayidle > /dev/null || ~/.config/hypr/scripts/swayidle.sh
    else
        echo "Invalid state: $state"
    fi
}

handle() {
  case $1 in
    screencast*) screencast "$1" ;;
  esac
}

socat -U - UNIX-CONNECT:/tmp/hypr/$HYPRLAND_INSTANCE_SIGNATURE/.socket2.sock | while read -r line; do handle "$line"; done

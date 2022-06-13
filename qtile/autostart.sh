#!/usr/bin/bash
picom -b
batsignal -w 25 -c 10 -d 5 &
xset s 350 120
xss-lock --transfer-sleep-lock -n 'bash /usr/share/doc/xss-lock/dim-screen.sh' -- betterlockscreen --off 15 -l blur &
/usr/bin/gnome-keyring-daemon --start --components=ssh,secrets,pkcs11 &
clight &
clipmenud &
polkit-dumb-agent &

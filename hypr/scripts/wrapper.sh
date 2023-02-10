#!/usr/bin/bash
export wrapperhl=true

export PATH=$PATH:/home/fabian/.local/bin
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
export XDG_DATA_HOME=$HOME/.local/share
export _JAVA_AWT_WM_NONREPARENTING=1
export XCURSOR_SIZE=24

# XDG Specifications
export XDG_CURRENT_DESKTOP=Hyprland
export XDG_SESSION_TYPE=wayland
export XDG_SESSION_DESKTOP=Hyprland

# QT Variables
export QT_AUTO_SCREEN_SCALE_FACTOR=1
export QT_QPA_PLATFORM="wayland;xcb"
#export QT_QPA_PLATFORMTHEME=qt5ct
#export QT_WAYLAND_DISABLE_WINDOWDECORATION=1

# Nvidia

if [[ "$1" == "nvidia" ]]; then 
    export LIBVA_DRIVER_NAME=nvidia
    export XDG_SESSION_TYPE=wayland
    export GBM_BACKEND=nvidia-drm
    export __GLX_VENDOR_LIBRARY_NAME=nvidia
    export WLR_NO_HARDWARE_CURSORS=1
    echo "Start with Nvidia-Card"
else 
    export WLR_NO_HARDWARE_CURSORS=1
    export __EGL_VENDOR_LIBRARY_FILENAMES=/usr/share/glvnd/egl_vendor.d/50_mesa.json # disabel all nvidia 
fi

exec Hyprland

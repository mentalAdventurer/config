#!/usr/bin/fish


#################
#  Keybindings  #
#################

fish_vi_key_bindings

# bind -M default j backward-char
# bind -M default k down-or-search 
# bind -M default l up-or-search
# bind -M default ö forward-char

# bind -M visual j backward-char
# bind -M visual k down-line
# bind -M visual l up-line
# bind -M visual ö forward-char

##################
#  Abbreviation  #
##################

abbr -a -U ra ranger
abbr -a -U xrandr2dp xrandr --output DP1-3 --mode 1920x1080 --primary --output eDP1 --mode 1920x1200 --right-of DP1-3

# Starship init
#starship init fish | source

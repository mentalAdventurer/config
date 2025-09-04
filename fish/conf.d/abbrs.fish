abbr --add gs 'git status --short'
abbr --add gsh 'git status --untracked-files=no --short'
abbr --add gl 'git log --graph --pretty=format:"%C(yellow)%h%Creset%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit --date=relative'
abbr --add gca 'git shortlog -sne | fzf --multi | cut -f2 -d (printf "\t") | sed \'s/^/Co-authored-by:\ /\''

abbr --add valhalla 'killall waybar && hyprctl keyword monitor DP-5,preferred,auto,2.0 && hyprctl keyword monitor DP-7,preferred,auto,2.0 && waybar > /dev/null 2>&1 & disown'

if type -q fdfind; and not type -q fd
    abbr --add fd 'fdfind'
end
if type -q batcat; and not type -q bat
    abbr --add bat 'batcat'
end

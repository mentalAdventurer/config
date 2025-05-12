abbr --add gs 'git status' 
abbr --add gsh 'git status --untracked-files=no'
abbr --add gl 'git log --graph --pretty=format:"%C(yellow)%h%Creset%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset" --abbrev-commit --date=relative'
abbr --add gca 'git shortlog -sne | fzf --multi | cut -f2 -d (printf "\t") | sed \'s/^/Co-authored-by:\ /\''

abbr --add lf 'lfcd'

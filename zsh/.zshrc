# Colors and Prompt
autoload -U colors && colors
PROMPT=" %{$fg[green]%}% %~ %{$reset_color%}  "

# Path
export PATH=$PATH:/home/fabian/.local/bin
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
export XDG_DATA_HOME=$HOME/.local/share

# Sources
source $HOME/.config/zsh/functions
source $HOME/.config/zsh/plugins
source $HOME/.config/zsh/alias


# History in cache directory
HISTSIZE=10000000
SAVEHIST=10000000
HISTFILE=~/.cache/zsh/history

# Basic auot/tab complete:
autoload -U compinit
zstyle ":completion:*" menu select
zmodload zsh/complist
compinit
_comp_options+=(globdots)

# zoxide
eval "$(zoxide init zsh)"

# Use vim keys in tab complete menu
bindkey -v

bindkey -M menuselect 'h' vi-backward-char
bindkey -M menuselect 'l' vi-forward-char
bindkey -M menuselect 'k' vi-up-line-or-history
bindkey -M menuselect 'j' vi-down-line-or-history

bindkey -M vicmd 'k' history-substring-search-up
bindkey -M vicmd 'j' history-substring-search-down

# remove delay entring normal mode
ZVM_READKEY_ENGINE=$ZVM_READKEY_ENGINE_NEX
ZVM_KEYTIMEOUT=0.001
ZVM_ESCAPE_KEYTIMEOUT=0.001

# Edit line in neovim 
autoload -U edit-command-line
# Emacs style
zle -N edit-command-line
bindkey '^xe' edit-command-line

eval "$(starship init zsh)"

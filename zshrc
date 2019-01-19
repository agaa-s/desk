# Set up the prompt
#autoload -Uz promptinit
#promptinit
## add kunihiko 2019-01-19 右寄せのプロンプトがでるテーマ
##prompt walters
#prompt adam1

# add kunihiko 2019-01-20 http://tegetegekibaru.blogspot.com/2012/08/zsh_2.html
# prompt %K背景色%k %F文字色%f %B太字%b
#autoload -U colors
#colors
PROMPT='%K{blue}%n@%m%k:%B%F{cyan}%.%f%b %# '
RPROMPT='%B%F{green}%~%f%b'

# Use emacs keybindings even if our EDITOR is set to vi
bindkey -e

# add kunihiko 2019-01-14 http://ama-ch.hatenablog.com/entry/20090109/1231526834
# ディレクトリ名を入力するだけで移動
setopt auto_cd
# 移動したディレクトリを記録しておく。"cd -[Tab]"で移動履歴を一覧
setopt auto_pushd
# pushdから重複を削除
setopt pushd_ignore_dups
# コマンド訂正
setopt correct
# 補完候補を詰めて表示する
setopt list_packed

setopt histignorealldups sharehistory

# Keep 1000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.zsh_history

# Use modern completion system
autoload -Uz compinit
compinit

# add kunihiko 2019-01-13
alias ls='ls --color'
alias ll='ls -l'
alias la='ls -a'
alias h='fc -lt "%F %T" -100'
alias cp='cp -i'
alias rm='rm -i'
alias back='popd'
alias cls='clear'
# グローバルエイリアス
alias -g L='| less'
alias -g H='| head'
alias -g G='| grep'
alias -g GI='| grep -ri'
alias -g M='| more'

# add kunihiko 2019-01-19
# cdの後にlsを実行
chpwd() { ls --color=auto }

# add kunihiko 2019-01-19
# cdrコマンドを有効 ログアウトしても有効なディレクトリ履歴
# cdr タブでリストを表示
autoload -Uz add-zsh-hook
autoload -Uz chpwd_recent_dirs cdr
add-zsh-hook chpwd chpwd_recent_dirs
# cdrコマンドで履歴にないディレクトリにも移動可能に
zstyle ":chpwd:*" recent-dirs-default true

zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' menu select=2
eval "$(dircolors -b)"
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true

zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh

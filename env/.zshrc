# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH
 export PATH="$HOME/bin:$HOME/anaconda3/bin:$PATH"

export TERM="xterm-256color"
# Path to your oh-my-zsh installation.
  export ZSH="/home/ctix/.oh-my-zsh"

export DART_SDK=$HOME/flutter/bin/cache/dart-sdk

# export flutter env variable for the china for installation
export PUB_HOSTED_URL="https://mirrors.tuna.tsinghua.edu.cn/dart-pub/"
export FLUTTER_STORAGE_BASE_URL="https://mirrors.tuna.tsinghua.edu.cn/flutter/"

export PATH=$PATH:$HOME/flutter/bin:$DART_SDK/bin:$HOME/.pub-cache/bin

export FCITX_SOCKET=/tmp/fcitx-remote.sock
# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
#ZSH_THEME="random"
ZSH_THEME="agnoster"
#ZSH_THEME="tonotdo"
#ZSH_THEME="candy"
#  good themes :  1.  re5et.zsh-theme

# Set list of themes to load
# Setting this variable when ZSH_THEME=random
# cause zsh load theme from this variable instead of
# looking in ~/.oh-my-zsh/themes/
# An empty array have no effect
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git wd z themes)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
 if [[ -n $SSH_CONNECTION ]]; then
   export EDITOR='vi'
 else
   export EDITOR='vi'
 fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
alias zshconfig="vi ~/.zshrc"
alias srczsh="source  ~/.zshrc"
alias ohmyzsh="vi ~/.oh-my-zsh"
alias lsdisk="sudo fdisk -l"
alias his="history|grep"
alias bjtime="sudo ntpdate 1.cn.pool.ntp.org"     
alias i3config="vi ~/.config/i3/config" 
alias pbd="ping -c4 www.baidu.com"
alias df="df -h"
alias wind="sudo mount /dev/sda5 /mnt/wind "
alias udisk="sudo mount -o rw /dev/sdb1 /mnt/udisk "
alias wine="sudo mount /dev/sda6 /mnt/wine"
alias ud="sudo mount /dev/sdb1 /mnt/udisk"
alias xres="xrdb -load ~/.Xresources"
alias xmmp="xmodmap ~/.Xmodmap"
alias alg="alias |grep"
alias ship="ip addr show"
alias skill="sudo kill -9"
alias svi="sudo vi"
alias jnb="jupyter lab"
alias vgao="xrandr --output VGA1 --auto --output LVDS1 --off"
alias loco="xrandr --output VGA1 --off --output LVDS1 --auto"
alias psg="ps -ef|grep"
#pacman search for files in which package
alias filepkg="yay -Qo" 
alias pkg2del="yay -Qdt" 
alias smbshare="sudo systemctl restart smb.service nmb.service"
alias find="find ./ -name" 
alias erect="xrandr -o left" 
alias zarc="vi ~/.config/zathura/zathurarc"
alias pspy="psg python"
#alias bgpix="feh -z --bg-scale ~/.wallpaper/*"
alias qtileconf="vi ~/.config/qtile/config.py" 
alias dudir="sudo du -h -d1"
alias hiworks="history |tail "
# tcvm been added to .ssh/config, so omit the port number
alias sshbiz="ssh ctix@tcvm"
alias sshsh="ssh ctix@shml"
alias bluepo="bluetoothctl power on"
alias dualvga="xrandr --output VGA1 --mode 1680x1050 -o left  --pos 0x0 --left-of LVDS1 --output LVDS1 --mode 1024x768 --right-of VGA1"
alias nfsup="sudo systemctl start nfs-server"
alias cha="cht.sh"
alias free="free -hm"

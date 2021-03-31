

## create xmodmap in your home
### 1 . Archlinux and Manjaro Version
```
> xmodmap -pke > ~/.Xmodmap
```

1. Mapping CapsLock to Left Control, and Shift+CapsLock mapping to CapsLock

inside  ~/.Xmodmap：
```
clear lock
clear control
add control = Caps_Lock Control_L Control_R
keycode 66 = Control_L Caps_Lock NoSymbol NoSymbol
```
2. Activating /Load the configuration
```
> xmodmap ~/.Xmodmap
```
3. Load and initialize ~/.xinitrc by append the following
```
if [ -f $HOME/.Xmodmap ]; then
    /usr/bin/xmodmap $HOME/.Xmodmap
fi
```
### 2. User setxkbmap cli, make a alias inside .bashrc or .zshrc

alias swcc="setxkbmap -option ctrl:swapcaps"

" let caps key modified as ctrls
setxkbmap -option caps:ctrl_modifier
" same as above 
setxkbmap -option ctrl:nocaps



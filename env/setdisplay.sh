!/bin/sh

case "$1" in
 vgao)
 xrandr --output VGA1 --auto --output LVDS1 --off
 ;;
 loco)
 xrandr --output VGA1 --off --output LVDS1 --auto
 ;;
 erect)
 xrandr --output VGA1 -o left
 ;;
 dual-erect)
 xrandr --output VGA1 --mode 1680x1050 -o left --pos 0x0 --right-of LVDS1 --output LVDS1 --mode 1024x768 --left-of VGA1
 ;;
 dual)
 xrandr --output VGA1 --mode 1680x1050 --pos 0x0 --right-of LVDS1 --output LVDS1 --mode 1024x768 --left-of VGA1
 ;;
 *) 
 echo "Usage ./setdisplay.sh vgao|loco|dual-erect|erect|dual"
 exit 1
 ;;
esac

exit 0

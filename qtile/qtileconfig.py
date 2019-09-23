# -*- coding: utf-8 -*-

from libqtile import bar, hook, layout, widget
from libqtile.command import lazy
from libqtile.config import Drag, Click, Group, Key, Match, Screen

# Theme defaults
bar_defaults = dict(
    size=28,
    background=['#222222', '#111111'],
)

layout_defaults = dict(
    border_width=1,
    margin=0,
    border_focus='#336699',
    border_normal='#333333',
)

widget_defaults = dict(
    font='Ubuntu',
    fontsize=14,
    padding=5,
    background=bar_defaults['background'],
    foreground=['#ffffff', '#ffffff', '#999999'],
    fontshadow='#000000',
)


class Widget(object):
    ''' Container for individual widget style options '''

    graph = dict(
        background='#000000',
        border_width=0,
        border_color='#000000',
        line_width=1,
        margin_x=0,
        margin_y=0,
        width=50,
    )

    groupbox = dict(
        active=widget_defaults['foreground'],
        inactive=['#444444', '#333333'],
        this_screen_border=layout_defaults['border_focus'],
        this_current_screen_border=layout_defaults['border_focus'],
        other_screen_border='#444444',
        urgent_text=widget_defaults['foreground'],
        urgent_border='#ff0000',
        highlight_method='block',
        rounded=True,

    # margin=-1,
        padding=3,
        borderwidth=2,
        disable_drag=True,
        invert_mouse_wheel=True,
    )

    sep = dict(
        foreground=layout_defaults['border_normal'],
        height_percent=100,
        padding=5,
    )

    systray = dict(
        icon_size=16,
        padding=5,
    )

    battery = dict(
        energy_now_file='charge_now',
        energy_full_file='charge_full',
        power_now_file='current_now',
    )

    battery_text = battery.copy()
    battery_text.update(
        charge_char='',    # fa-arrow-up
        discharge_char='',    # fa-arrow-down
        format='{char} {hour:d}:{min:02d}',
    )

    weather = dict(
        update_interval=60,
        metric=False,
        format='{condition_text} {condition_temp}°',
    )


# Commands to spawn
class Commands(object):
    browser = 'opera'
    dmenu = 'dmenu_run -i -b -p ">>>" -fn "-*-fixed-*-*-*-*-16-*-*-*-*-*-*-*" -nb "#15181a" -nf "#fff" -sb "#333" -sf "#fff"'
    file_manager = 'thunar'
    lock_screen = 'i3exit lock'
    suspend_sys = 'systemctl suspend'
    changebg = 'feh --randomize --bg-scale /home/ctix/Pictures/*'

    # screenshot = 'gnome-screenshot'
    terminal = 'urxvt'
    # trackpad_toggle = "synclient TouchpadOff=$(synclient -l | grep -c 'TouchpadOff.*=.*0')"
    #volume_up = 'amixer -q -c 1 sset Master 5dB+'
    #volume_down = 'amixer -q -c 1 sset Master 5dB-'
    volume_toggle = 'amixer -q -D pulse sset Master 1+ toggle'


# Keybindings
mod = 'mod4'
keys = [
    # Window Manager Controls
    Key([mod, 'control'], 'r', lazy.restart()),
    Key([mod, 'control'], 'q', lazy.shutdown()),
    Key([mod, 'control'], 'l', lazy.spawn(Commands.lock_screen)),
    Key([mod, 'control'], 'x', lazy.spawn(Commands.suspend_sys)),

    # Window Controls
    Key([mod, 'shift'], 'q', lazy.window.kill()),
    Key([mod, 'shift'], 'f', lazy.window.toggle_fullscreen()),
    Key([mod], 'f', lazy.window.toggle_floating()),

    # Layout, group, and screen modifiers
    Key([mod], 'k', lazy.layout.up()),
    Key([mod], 'j', lazy.layout.down()),
    Key([mod, 'shift'], 'k', lazy.next_layout()),
    Key([mod, 'shift'], 'j', lazy.prev_layout()),
    #Key([mod, 'shift'], 'g', lazy.layout.grow()),
    #Key([mod, 'shift'], 's', lazy.layout.shrink()),
    #Key([mod, 'shift'], 'n', lazy.layout.normalize()),
    #Key([mod, 'shift'], 'm', lazy.layout.maximize()),

    # Switch groups
    Key([mod], 'h', lazy.screen.prev_group()),
    Key([mod], 'l', lazy.screen.next_group()),
    Key([mod, 'shift'], 'space', lazy.screen.toggle_group()),

    # Cycle layouts
    #Key([mod], 'Up', lazy.next_layout()),
    #Key([mod], 'Down', lazy.prev_layout()),

    # Change window focus
    Key([mod], 'Tab', lazy.layout.next()),
    Key([mod, 'shift'], 'Tab', lazy.next_layout()),

    # Switch focus to other screens
    #Key([mod, 'shift'], 'h', lazy.to_screen(0)),    # left
    #Key([mod, 'shift'], 'l', lazy.to_screen(1)),    # right

    # Commands: Application Launchers
    Key([mod], 'space', lazy.spawn(Commands.dmenu)),
    Key([mod], 'b', lazy.spawn(Commands.browser)),
    Key([mod], 'e', lazy.spawn(Commands.file_manager)),
    Key([mod], 'p', lazy.spawn(Commands.changebg)),
    Key([mod], 'Return', lazy.spawn(Commands.terminal)),

    # Commands: Volume Controls
    #Key([], 'XF86AudioRaiseVolume', lazy.spawn(Commands.volume_up)),
    #Key([], 'XF86AudioLowerVolume', lazy.spawn(Commands.volume_down)),
    Key([], 'XF86AudioMute', lazy.spawn(Commands.volume_toggle)),
    #Key([], 'XF86TouchpadToggle', lazy.spawn(Commands.trackpad_toggle)),

    # TODO: What does the PrtSc button map to?
    #Key([mod], 'p', lazy.spawn(Commands.screenshot)),
]

# Groups
group_setup = (
    ('', {  # fa-globe
        'layout': 'max',
        'matches': [Match(wm_class=('Opera', 'Google-chrome'))],
    }),
    ('', {  # fa-code
        'layout': 'max',
        'matches': [Match(wm_class=('Vim',))],
    }),
    ('', {}),  # fa-terminal
    ('', {
            'layout': 'max',
            'matches': [Match(wm_class=('Sakura',))],
             }),
    ('', {  # fa-windows
        'layout': 'max',
        'matches': [Match(wm_class=('Chromium',))],
    }),
    ('', {  # fa-steam
        'layout': 'max',
        'matches': [Match(wm_class=('Thunar',))],
    }),
    ('', {}),  # fa-circle-o
    ('', {
        'layout': 'max',
        'matches': [Match(wm_class=('Visual Studio'))],
            }),  # fa-dot-circle-o
    ('', {  # fa-circle
        'layout': 'max',
        'matches': [Match(wm_class=('Zathura',))],
    }),
)

groups = []
for idx, (label, config) in enumerate(group_setup):
    hotkey = str(idx + 1)
    config.setdefault('layout', 'tile')
    groups.append(Group(label, **config))

    # mod + hotkey = switch to group
    keys.append(Key([mod], hotkey, lazy.group[label].toscreen()))

    # mod + shift + hotkey = move focused window to group
    keys.append(Key([mod, 'shift'], hotkey, lazy.window.togroup(label)))

# Mouse
mouse = (
    Drag([mod],
         'Button1',
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod],
         'Button3',
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
)

def num_screens():
    process = subprocess.Popen(["xrandr"], stdout=subprocess.PIPE)
    out = process.communicate()[0].split("\n")
    i = 0
    for line in out:
        if " connected " in line:
            i += 1
        return i

bring_front_click = True

# Screens
screens = [
    Screen(
     #bottom=bar.Bar(widgets=[Powerline()], **bar_defaults),
        top=bar.Bar(
            widgets=[
                widget.GroupBox(**Widget.groupbox),
                widget.Clock(foreground='4aef81', format='%y-%m-%d %H:%M'),
                widget.Sep(**Widget.sep),
                widget.WindowName(),
                widget.CPUGraph(
                    graph_color='#18BAEB',
                    fill_color='#1667EB.3',
                    **Widget.graph),
    #  widget.MemoryGraph(
    #  graph_color='#00FE81',
    #  fill_color='#00B25B.3',
    #  **Widget.graph),
    #  widget.SwapGraph(
    #  graph_color='#5E0101',
    #  fill_color='#FF5656',
    #  **Widget.graph),
                widget.NetGraph(
                    graph_color='#ffff00',
                    fill_color='#4d4d00',
                    interface='wls3',
                    **Widget.graph),
    # widget.HDDBusyGraph(device='sda', **Widget.graph),
    #  widget.HDDBusyGraph(device='sdb', **Widget.graph),
                widget.ThermalSensor(metric=True, threshold=79),
                widget.Sep(**Widget.sep),
                widget.CurrentLayout(),
                widget.Systray(**Widget.systray),
                widget.BatteryIcon(**Widget.battery),
    #widget.Battery(**Widget.battery_text),
    #widget.Volume(
    #     theme_path='/usr/share/icons/Humanity/status/22/',
    #     cardid=1),
    #widget.YahooWeather(location='Beijing, CN', **Widget.weather),
    #widget.Wlan(interface='wls3'),
            ],
            **bar_defaults), ),
   # Screen(
   #     top=bar.Bar(
   #         widgets=[
   #             widget.GroupBox(**Widget.groupbox),
   #             widget.WindowName(),
   #             widget.CurrentLayout(),
   # #  Widget.Battery(),
   #         ],
   #         **bar_defaults), )
]

if num_screens() == 2:
    screens.append(
    Screen(
    bottom=bar.Bar([
    widget.GroupBox(highlight_method="block", this_current_screen_border=colors["blue"]),
	widget.Sep(padding=15),
	widget.CurrentLayout(),
	widget.Sep(padding=15),
	widget.Prompt(),
	_WindowTabs(),
	widget.Systray(),
	], 25)))

# Layouts
layouts = (
    layout.Tile(ratio=0.5, **layout_defaults),
    layout.Max(**layout_defaults),
    layout.RatioTile(**layout_defaults),
    layout.Matrix(**layout_defaults),
    layout.MonadTall(**layout_defaults),
    layout.Stack(**layout_defaults),
    layout.Zoomy(**layout_defaults),
)

floating_layout = layout.floating.Floating(
    auto_float_types=(
        'notification',
        'toolbar',
        'splash',
        'dialog',
    ),
    float_rules=[
        {
            'wmclass': x
        } for x in (
            'audacious',
            'Download',
            'dropbox',
            'file_progress',
            'file-roller',
            'gimp',
            'Komodo_confirm_repl',
            'Komodo_find2',
            'pidgin',
            'skype',
            'Transmission',
            'Update',    # Komodo update window
            'Xephyr',
        )
    ],
    **layout_defaults)


def main(qtile):
    import os
    os.system("nm-applet &")
    os.system("~/.wallpaper/changebg.sh")
    os.system("fcitx -d &")
    os.system("volumeicon &")
    pass


@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

from libqtile.bar import Bar

from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.wlan import Wlan
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.pulse_volume import PulseVolume
from libqtile.widget.spacer import Spacer
from libqtile.widget.sep import Sep
from libqtile.widget.textbox import TextBox
from libqtile.widget.battery import Battery, BatteryIcon, BatteryState
from libqtile.widget.backlight import Backlight


from colors import gruvbox
from unicodes import left_half_circle, right_half_circle

bar = Bar([
    Spacer(length=10),
    GroupBox(
        font="TerminessTTF Nerd Font Bold",
        disable_drag=True,
        active=gruvbox['fg'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['magenta'],
        this_current_screen_border=gruvbox['magenta'],
        this_screen_border=gruvbox['fg'],
        other_current_screen_border=gruvbox['magenta'],
        other_screen_border=gruvbox['fg'],
        borderwidth=1.5,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),

    Spacer(length=10),
    Sep(
        foreground=gruvbox['fg'],
        line_width=9,
        size_percent=70,
    ),
    Spacer(length=10),

    CurrentLayout(
        background=gruvbox['bg'],
        foreground=gruvbox['dark-green'],
    ),

    Spacer(length=10),

    WindowCount(
        text_format='缾 {num}',
        background=gruvbox['bg'],
        foreground=gruvbox['dark-red'],
        show_zero=True
    ),

    Spacer(length=10),


    WindowName(foreground=gruvbox['fg'],format=""),


    Spacer(length=10),

    Backlight(
        foreground=gruvbox['dark-yellow'],
        background=gruvbox['bg'],
        format='盛 {percent:2.0%}',
        backlight_name="intel_backlight"),

    Spacer(length=10),

    Sep(
        foreground=gruvbox['fg'],
        line_width=9,
        size_percent=70,
    ),

    Spacer(length=10),

    TextBox(
        text=" ",
        foreground=gruvbox['dark-red'],
        background=gruvbox['bg'],
    ),

    PulseVolume(
        foreground=gruvbox['dark-red'],
        background=gruvbox['bg'],
        update_interval=0.2
    ),

    Spacer(length=10),

    Sep(
        foreground=gruvbox['fg'],
        line_width=9,
        size_percent=70,
    ),

    Spacer(length=10),

    TextBox(
        text="ﲮ",
        foreground=gruvbox['dark-magenta'],
        background=gruvbox['bg'],
    ),

    Memory(
        format='{MemUsed: 1.0f}{mm} /{MemTotal: 1.0f}{mm}',
        foreground=gruvbox['dark-magenta'],
        background=gruvbox['bg'],
        measure_mem='G'
    ),

    Spacer(length=10),

    Sep(
        foreground=gruvbox['fg'],
        line_width=9,
        size_percent=70,
    ),

    Spacer(length=10),

    Wlan(
        foreground=gruvbox['dark-blue'],
        background=gruvbox['bg'],
        interface="wlp0s20f3",
        format='{essid} {percent:2.0%}'
    ),

    #Net(
    #    foreground=gruvbox['dark-blue'],
    #    background=gruvbox['bg'],
    #    format="{down} ↓↑{up}",
    #    prefix="M"
    #),

    Spacer(length=10),

    Sep(
        foreground=gruvbox['fg'],
        line_width=9,
        size_percent=70,
    ),

    Spacer(length=10),

    Battery(
        background=gruvbox["bg"],
        foreground=gruvbox["dark-green"],
        format=' {percent:2.0%} {watt:.2f}W'),

    Spacer(length=10),

    Sep(
        foreground=gruvbox['fg'],
        line_width=9,
        size_percent=70,
    ),

    Spacer(length=10),

    Clock(
        background=gruvbox['bg'],
        foreground=gruvbox['fg'],
        format=' %d %a %I:%M'),

    Spacer(length=10),
],
    margin=[10, 10, 5, 10],
    background=gruvbox["bg"],
    opacity=1,
    size=25,
)

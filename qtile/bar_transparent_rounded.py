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
from libqtile.widget.textbox import TextBox
from libqtile.widget.battery import Battery, BatteryIcon, BatteryState
from libqtile.widget.backlight import Backlight


from colors import gruvbox
from unicodes import left_half_circle, right_half_circle

bar = Bar([
    left_half_circle(gruvbox['bg']),
    GroupBox(
        disable_drag=True,
        active=gruvbox['fg'],
        inactive=gruvbox['dark-gray'],
        highlight_method='line',
        block_highlight_text_color=gruvbox['magenta'],
        borderwidth=0,
        highlight_color=gruvbox['bg'],
        background=gruvbox['bg']
    ),
    right_half_circle(gruvbox['bg']),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-blue']),
    CurrentLayout(
        background=gruvbox['dark-blue'],
    ),
    right_half_circle(gruvbox['dark-blue']),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-magenta']),
    WindowCount(
        text_format='缾 {num}',
        background=gruvbox['dark-magenta'],
        show_zero=True
    ),
    right_half_circle(gruvbox['dark-magenta']),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-cyan']),
    Clock(
        background=gruvbox['dark-cyan'],
        format=' %d %a %I:%M'),
    right_half_circle(gruvbox['dark-cyan']),

    Spacer(length=10),

    WindowName(foreground=gruvbox['fg'],format=""),

    Spacer(length=10),

    left_half_circle(gruvbox['dark-magenta']),
    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=gruvbox['dark-magenta']),
    right_half_circle(gruvbox['dark-magenta']),

    Spacer(length=10),
    left_half_circle(gruvbox['yellow']),
    Backlight(
        background=gruvbox['yellow'],
        format='  {percent:2.0%}',
        backlight_name="intel_backlight"),
    right_half_circle(gruvbox['yellow']),

    Spacer(length=10),
    left_half_circle(gruvbox['red']),
    TextBox(text=" ",background=gruvbox['red']),
    PulseVolume(background=gruvbox['red'],update_interval=0.2),
    right_half_circle(gruvbox['red']),
    Spacer(length=10),

    left_half_circle(gruvbox['dark-blue']),
    Wlan(
        background=gruvbox['dark-blue'],
        interface="wlp0s20f3",
        format='{essid} {percent:2.0%}'
    ),

    Net(
        background=gruvbox['dark-blue'],
        format="{down} ↓↑ {up}",
    ),
    right_half_circle(gruvbox['dark-blue']),

    Spacer(length=10),
    left_half_circle(gruvbox['dark-cyan']),
    Battery(
        background=gruvbox["dark-cyan"],
        format=' {percent:2.0%} {watt:.2f}W'),
    right_half_circle(gruvbox['dark-cyan'])
],
    margin=[10, 10, 5, 10],
    background='#00000000',
    opacity=1,
    size=25,
)

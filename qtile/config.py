import os
import subprocess
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile import hook
from libqtile.utils import guess_terminal

from colors import gruvbox
from bar_transparent_rounded import bar

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "odiaeresis", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "l", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "odiaeresis", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "j", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "odiaeresis", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "k", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "l", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod, "mod1"], "j", lazy.layout.flip_left()),
    Key([mod, "mod1"], "odiaeresis", lazy.layout.flip_right()),
    Key([mod, "mod1"], "k", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_up()),
    Key([mod, "shift"], "n", lazy.layout.normalize()),
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),

    # Toggle floating and fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle floating"),

    Key([mod, "shift"], "BackSpace", lazy.spawn("xrandr --auto"), desc="Toggle floating"),
    Key([mod, "control"], "BackSpace", lazy.spawn("xrandr --output eDP1 --off"), desc="Toggle floating"),
    Key([mod], "z", lazy.spawn("loginctl lock-session"), desc="Toggle floating"),

    # Functionkeys
    Key([], "XF86AudioRaiseVolume", lazy.spawn("changeVolume +3%"), desc="Raise Volume"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("changeVolume -3% "), desc="Raise Volume"),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"), desc="Raise Volume"),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Raise Volume"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Raise Volume"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Raise Volume"),
    Key([], "XF86MonBrightnessDown", lazy.spawn("changeBrightness 3%-"), desc="Raise Volume"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("changeBrightness +3%"), desc="Raise Volume"),
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Raise Volume"),


    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], 'd', lazy.run_extension(extension.DmenuRun(
            font="TerminessTTF Nerd Font",
            fontsize="13",
            dmenu_command="dmenu_run",
            dmenu_prompt=" ",
            dmenu_height=10,
            dmenu_lines=15,
            background=gruvbox['bg'],
            foreground=gruvbox['fg'],
            selected_foreground=gruvbox['dark-blue'],
            selected_background=gruvbox['bg'],
        ))),
]

groups = [
    Group('1', label="一", layout="monadtall"),
    Group('2', label="二", layout="bsp"),
    Group('3', label="三", layout="bsp"),
    Group('4', label="四", layout="bsp"),
    Group('5', label="五", layout="bsp"),
    Group('6', label="六", layout="bsp"),
    Group('7', label="七", layout="bsp"),
    Group('8', label="八", layout="bsp"),
    Group('9', label="九", layout="max"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('term', 'alacritty', width=0.4, height=0.5, x=0.3, y=0.1, opacity=1),
    DropDown('mixer', 'pavucontrol', width=0.4,
             height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('bitwarden', 'bitwarden-desktop',
             width=0.5, height=0.55, x=0.25, y=0.2, opacity=1),
    DropDown('notetaker', 'alacritty -e fish -c notetaker_qtile',
             width=0.586, height=0.624, x=0.2075, y=0.15, opacity=1),
    DropDown('calendar', 'gnome-calendar',
             width=0.586, height=0.624, x=0.2075, y=0.15, opacity=1),
]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('mixer')),
    Key([mod], "p", lazy.group['scratchpad'].dropdown_toggle('bitwarden')),
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('notetaker')),
    Key([mod], "g", lazy.group['scratchpad'].dropdown_toggle('calendar')),
])

layouts = [
    layout.Bsp(lower_right=True,margin=5,fair=False),
    layout.MonadTall(ratio=0.68,margin=4,max_ration=1,min_ration=0,single_border_width=0),
    layout.Max(),
]

widget_defaults = dict(
    font='TerminessTTF Nerd Font',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar,
        wallpaper="~/Pictures/Wallpaper/wp5071587.jpg",
        wallpaper_mode="fill"
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

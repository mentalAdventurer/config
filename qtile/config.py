import os
import subprocess
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy
from libqtile import hook

from colors import gruvbox
from bar_transparent_rounded import bar

mod = "mod4"
terminal = "kitty" 

keys = [
    # Switch between windows
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "odiaeresis", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "l", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h", lazy.group.prev_window(), desc="Move to prev Window"),
    Key([mod], "adiaeresis", lazy.group.next_window(), desc="Move to next Window"),
    Key([mod], "space",lazy.next_screen()),

    # Move Windows
    Key([mod, "shift"], "j", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "odiaeresis", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "mod1"], "j", 
        lazy.layout.flip_left(),
        lazy.layout.swap_column_left().when(layout="columns")),
    Key([mod, "mod1"], "odiaeresis", 
        lazy.layout.flip_right(),
        lazy.layout.swap_column_right().when(layout="columns")),
    Key([mod, "mod1"], "k", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_up()),

    # Resize
    Key([mod, "control"], "j", 
        lazy.layout.grow_left().when(layout="bsp"), 
        lazy.layout.shrink_main().when(layout="monadtall"),
        desc="Grow window to the left"),
    Key([mod, "control"], "odiaeresis",
        lazy.layout.grow_right().when(layout="bsp"), 
        lazy.layout.grow_main().when(layout="monadtall"),
        desc="Grow window to the right"),
    Key([mod, "control"], "k", 
        lazy.layout.grow_down().when(layout="bsp"), 
        lazy.layout.grow().when(layout="monadtall"),
        desc="Grow window down"),
    Key([mod, "control"], "l", 
        lazy.layout.grow_up().when(layout="bsp"), 
        lazy.layout.shrink().when(layout="monadtall"),
        desc="Grow window up"),
    Key([mod, "control"], "n", lazy.layout.normalize()),

    # Toggle floating and fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc="Toggle floating"),

    Key([mod, "shift"], "BackSpace", lazy.spawn("dmenu_screen"), desc="Toggle floating"),
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
        [mod],
        "e",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "e", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "c", lazy.spawn("clipmenu"),desc="launch clipmenu"),
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
    Group('1', label="α", layout="monadtall"),
    Group('2', label="β", layout="bsp"),
    Group('3', label="γ", layout="bsp"),
    Group('4', label="δ", layout="bsp"),
    Group('5', label="ε", layout="bsp"),
    Group('6', label="δ", layout="bsp"),
    Group('7', label="η", layout="bsp"),
    Group('8', label="λ", layout="bsp"),
    Group('9', label="π", layout="columns"),
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
    DropDown('term', 'kitty',
             width=0.586, height=0.624, x=0.2075, y=0.15, opacity=1),
    DropDown('mixer', 'pavucontrol', width=0.4,
             height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('bitwarden', 'bitwarden-desktop',
             width=0.5, height=0.55, x=0.25, y=0.2, opacity=1),
    DropDown('notetaker', 'kitty fish -c notetaker_qtile',
             width=0.586, height=0.624, x=0.2075, y=0.15, opacity=1),
    DropDown('calendar', 'gnome-calendar',
             width=0.586, height=0.624, x=0.2075, y=0.15, opacity=1),
    DropDown('ranger', 'kitty ranger', 
             width=0.586, height=0.624, x=0.2075, y=0.15, opacity=1),
]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('mixer')),
    Key([mod], "p", lazy.group['scratchpad'].dropdown_toggle('bitwarden')),
    Key([mod], "n", lazy.group['scratchpad'].dropdown_toggle('notetaker')),
    Key([mod], "g", lazy.group['scratchpad'].dropdown_toggle('calendar')),
    Key([mod], "r", lazy.group['scratchpad'].dropdown_toggle('ranger')),
])

layouts = [
    layout.Bsp(lower_right=True,margin=7,fair=False),
    layout.MonadTall(ratio=0.68,margin=7,max_ration=1,min_ration=0,single_border_width=0),
    layout.Columns(margin=7),
    #layout.Stack(num_stacks=1, margin=7, border_focus="#881111",border_width=0),
]

widget_defaults = dict(
    font='JetBrainsMonoMedium Nerd Font Medium',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar,
        wallpaper="~/.config/qtile/img/wallpaper1.jpg",
        wallpaper_mode="fill"
    ),
    Screen(
        wallpaper="~/.config/qtile/img/wallpaper2.jpg",
        wallpaper_mode="fill"
    ),

]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_normal=gruvbox['dark-gray'],
    border_focus=gruvbox['dark-blue'],
    border_width=3,
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
floats_kept_above = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])

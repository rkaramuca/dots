# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

################################################################################
import os
import subprocess
from libqtile import hook
# startup hooks
@hook.subscribe.startup_once
def autostart():
	home = os.path.expanduser('~/.config/qtile/autostart.sh')
	subprocess.call([home])

################################################################################

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

	# Swap left and right columns in the Column layout
	Key([mod, "shift", "control"], "h", lazy.layout.swap_column_left()),
	Key([mod, "shift", "control"], "l", lazy.layout.swap_column_right()),
	
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    #Key([mod], "r", lazy.spawncmd(),
        #desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("dmenu_run -p Vampire -fn 'Ubuntu Mono:regular:pixelsize=18' -nb '#282a36' -nf '#caa9fa' -sf '#282a36' -sb '#8be9fd'"),
        desc="Runs dmenu"),

	# Custom Keybinds ##########################################################
	# Application Launches
	Key([mod], "b", lazy.spawn("firefox"), desc="Launch Firefox"),
	Key([mod], "c", lazy.spawn("code"), desc="Launch VSCode"),
	Key([mod], "d", lazy.spawn("discord"), desc="Launch Discord"),
	Key([mod], "s", lazy.spawn("spotify"), desc="Launch Spotify"),
	Key([mod], "v", lazy.spawn("pavucontrol"), desc="Launch PavuControl Audio"),
	# Screen Shot
	Key([mod], "p", lazy.spawn("flameshot gui"), desc="Screenshot via flameshot"),
	# Audio Controls
	# Master/Speaker Volume?
	Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 2 -q set Master 2%+"), desc="Speaker volume increase"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 2 -q set Master 2%-"), desc="Speaker volume decrease"),
	Key([], "XF86AudioMute", lazy.spawn("amixer -c 2 -q set Master toggle"), desc="Speaker volume mute"),
	# Backlight Controls
	Key([mod], "period", lazy.spawn("brightnessctl -s set +10"), desc="Backlight increase"),
	Key([mod], "comma", lazy.spawn("brightnessctl -s set 10-"), desc="Backlight decrease"),
	# Launch WiFi Controller
    Key([mod], "i", lazy.spawn("networkmanager_dmenu -p Vampire -fn 'Ubuntu Mono:regular:pixelsize=18' -nb '#282a36' -nf '#caa9fa' -sf '#272a36' -sb '#8be9fd'"),
		desc="Runs dmenu NetworkManager Applet"),
	############################################################################
]

# Colors List
def init_colors():
	return [["#282a36", "#282a36"], # panel background (gray)
    		["#caa9fa", "#caa9fa"], # light purple
          	["#f8f8f2", "#f8f8f2"], # font color for selected group (white-ish)
           	["#8be9fd", "#8be9fd"], # light blue
           	["#ff92d0", "#ff92d0"]] # secondary/other group color (pink)
colors = init_colors()

#groups = [Group(i) for i in "12345"]
# Changed group labels to "Font Awesome" icons, still targeted by first parameter
groups = [
	Group("1", label="", ),
	Group("2", label="︁"),
	Group("3", label="︁"),
	Group("4", label=""),
	Group("5", label=""),
	Group("6", label=""),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
	# margin=8 adds gaps of size 8
    layout.Columns(
		border_focus='#8be9fd',
		border_focus_stack='#8be9fd',
		border_normal='#caa9fa',
		border_normal_stack='#caa9fa',
		border_on_single='#caa9fa',
		border_width=6,
		insert_position=1,
		margin=8,
		),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    #layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=14,
    padding=2,
	background=colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
		# add bar to the top of the screen
		top=bar.Bar(
			[
				widget.Sep(
					linewidth=0,
					padding=6,
					background=colors[3]
					),
				widget.CurrentLayout(padding=5),
				# display the current group
				widget.GroupBox(
					margin_y=3,
					margin_x=0,
					padding_y=5,
					padding_x=3,
					borderwidth=3,
					# any group with an open window will be white, otherwise purple
					active=colors[2],
					inactive=colors[1],
					rounded=False,
					# blue background if active
					highlight_color=colors[3],
					highlight_method="line",
					# group "1" gets a pink underline, group "2" gets a blue underline
					this_current_screen_border=colors[4],
					this_screen_border=colors[3],
					other_current_screen_border=colors[4],
					other_screen_border=colors[3],
					foreground=colors[2],
					background=colors[0]
					),
				widget.Prompt(),
				# display the name of the window with focus
				# widget.WindowName(),
				widget.Chord(
					chords_colors={
						'launch': ("#ff0000", "#ffffff"),
					},
					name_transform=lambda name: name.upper(),
				),
				#widget.Systray(),

				# Creates a spacer that is equal to the right alignment of the widgets
				widget.Spacer(length=bar.STRETCH),
				# Add Volume with arrow
				widget.TextBox(text="", foreground=colors[1], padding=0, fontsize=41),
				widget.TextBox(text="", foreground=colors[0], background=colors[1]),
				widget.Volume(foreground=colors[0], background=colors[1], padding=5),
				# Add Network information with arrow
				widget.TextBox(text="", foreground=colors[3], background=colors[1], padding=0, fontsize=41),
				widget.Wlan(foreground=colors[0], background=colors[3], padding=5, disconnected_message='None :(', format='  {quality}/70'),
				# Add Disk space with arrow
				widget.TextBox(text="", foreground=colors[1], background=colors[3], padding=0, fontsize=41),
				widget.DF(foreground=colors[0], background=colors[1], visible_on_warn=False, format='{p}: {uf}{m}|{r:.0f}%'),
				# Add Battery Status with arrow
				widget.TextBox(text="", foreground=colors[3], background=colors[1], padding=0, fontsize=41),
				widget.Battery(
					charge_char="",
					discharge_char="",
					empty_char="",
					full_char="",
					show_short_text=False,
					low_foreground=colors[4],
					foreground=colors[0], 
					background=colors[3], 
					padding=5, 
					format='{char} {percent: 2.0%}'
					),
				# Add Clock with arrow
				widget.TextBox(text="", foreground=colors[1], background=colors[3], padding=0, fontsize=41),
				widget.TextBox(text='', foreground=colors[0], background=colors[1]),
				widget.Clock(foreground=colors[0], background=colors[1], padding=5, format='%A, %B, %d - %H:%M '),
				# Little Icon on the right
				widget.TextBox(text="", foreground=colors[3], background=colors[1], padding=0, fontsize=41),
				widget.TextBox(text="", foreground=colors[0], background=colors[3])
			],
			20,
			background=colors[0],
		),
	),

	Screen(
		# add bar to the top of the screen
		top=bar.Bar(
			[
				widget.Sep(
					linewidth=0,
					padding=6,
					background=colors[3]
					),
				widget.CurrentLayout(padding=5),
				# display the current group
				widget.GroupBox(
					margin_y=3,
					margin_x=0,
					padding_y=5,
					padding_x=3,
					borderwidth=3,
					# any group with an open window will be white, otherwise purple
					active=colors[2],
					inactive=colors[1],
					rounded=False,
					# blue background if active
					highlight_color=colors[3],
					highlight_method="line",
					# group "1" gets a pink underline, group "2" gets a blue underline
					this_current_screen_border=colors[4],
					this_screen_border=colors[3],
					other_current_screen_border=colors[4],
					other_screen_border=colors[3],
					foreground=colors[2],
					background=colors[0]
					),
				widget.Prompt(),
				# display the name of the window with focus
				# widget.WindowName(),
				widget.Chord(
					chords_colors={
						'launch': ("#ff0000", "#ffffff"),
					},
					name_transform=lambda name: name.upper(),
				),

				# Create a Systray for WiFi/Volume
				#widget.TextBox(text="", foreground=colors[3], padding=0, fontsize=41),
				#widget.Systray(background=colors[3]),
				
				# Creates a spacer that is equal to the right alignment of the widgets
				widget.Spacer(length=bar.STRETCH),
				# Add Volume with arrow
				widget.TextBox(text="", foreground=colors[1], padding=0, fontsize=41),
				widget.TextBox(text="", foreground=colors[0], background=colors[1]),
				widget.Volume(foreground=colors[0], background=colors[1], padding=5),
				# Add Network information with arrow
				widget.TextBox(text="", foreground=colors[3], background=colors[1], padding=0, fontsize=41),
				widget.Wlan(foreground=colors[0], background=colors[3], padding=5, disconnected_message='None :(', format='  {quality}/70'),
				# Add Disk space with arrow
				widget.TextBox(text="", foreground=colors[1], background=colors[3], padding=0, fontsize=41),
				widget.DF(foreground=colors[0], background=colors[1], visible_on_warn=False, format='{p}: {uf}{m}|{r:.0f}%'),
				# Add Battery Status with arrow
				widget.TextBox(text="", foreground=colors[3], background=colors[1], padding=0, fontsize=41),
				widget.Battery(
					charge_char="",
					discharge_char="",
					empty_char="",
					full_char="",
					show_short_text=False,
					low_foreground=colors[4],
					foreground=colors[0], 
					background=colors[3], 
					padding=5, 
					format='{char} {percent: 2.0%}'
					),
				# Add Clock with arrow
				widget.TextBox(text="", foreground=colors[1], background=colors[3], padding=0, fontsize=41),
				widget.TextBox(text='', foreground=colors[0], background=colors[1]),
				widget.Clock(foreground=colors[0], background=colors[1], padding=5, format='%A, %B, %d - %H:%M '),
				# Little Icon on the right
				widget.TextBox(text="", foreground=colors[3], background=colors[1], padding=0, fontsize=41),
				widget.TextBox(text="", foreground=colors[0], background=colors[3])
			],
			20,
			background=colors[0],
		),
	),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

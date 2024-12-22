from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration


mod = "mod1"
supr = "mod4"
terminal = "alacritty"
rofi = "/home/grey/.config/rofi/launchers/type-1/launcher.sh"
browser = "chromium"

def RD(hex,corner=None) -> object: 
	return RectDecoration( 
	    radius = 0 if corner is None else corner,
        filled = True, colour = hex, padding = 4, )

keys = [
    Key([mod],"h",lazy.layout.left(),desc="Move focus to left"),
    Key([mod],"l",lazy.layout.right(),desc="Move focus to right"),
    Key([mod],"j",lazy.layout.down(),desc="Move focus down"),
    Key([mod],"k",lazy.layout.up(),desc="Move focus up"),
    Key([mod],"space",lazy.layout.next(),desc="Move window focus to other window"),
    Key([mod,"shift"],"h",lazy.layout.shuffle_left(),desc="Move window to the left"),
    Key([mod,"shift"],"l",lazy.layout.shuffle_right(),desc="Move window to the right"),
    Key([mod,"shift"],"j",lazy.layout.shuffle_down(),desc="Move window down"),
    Key([mod,"shift"],"k",lazy.layout.shuffle_up(),desc="Move window up"),
    Key([mod,"control"],"h",lazy.layout.grow_left(),desc="Grow window to the left"),
    Key([mod,"control"],"l",lazy.layout.grow_right(),desc="Grow window to the right"),
    Key([mod,"control"],"j",lazy.layout.grow_down(),desc="Grow window down"),
    Key([mod,"control"],"k",lazy.layout.grow_up(),desc="Grow window up"),
    Key([mod],"n",lazy.layout.normalize(),desc="Reset all window sizes"),
    Key([mod,"shift"],"Return",lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack",),
    Key([mod],"Return",lazy.spawn(terminal),desc="Launch terminal"),
    Key([mod],"p",lazy.spawn(rofi),desc="Run rofi"),
    Key([mod],"b",lazy.spawn(browser),desc="Open Librewolf"),
    Key([],"Print",lazy.spawn("flameshot gui"),desc="Prt sc"),
    Key([mod],"Tab",lazy.next_layout(),desc="Toggle between layouts"),
    Key([mod],"q",lazy.window.kill(),desc="Kill focused window"),
    Key([mod],"f",lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window",),
    Key([mod],"t",lazy.window.toggle_floating(),desc="Toggle floating on the focused window"),
    Key([mod,"shift"],"r",lazy.reload_config(),desc="Reload the config"),
    Key([mod,"shift"],"q",lazy.shutdown(),desc="Shutdown Qtile"),
    Key([mod,"shift"],"x",lazy.spawn("i3lock -i /home/grey/wallpapers/gruv/gruv-aurora.png -R 125"),desc="Spawn i3-lock"),
    Key([mod],"r",lazy.spawncmd(),desc="Spawn a command using a prompt widget"),
    Key([],"XF86AudioLowerVolume",lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -2%"),desc="Lowers volume"),
    Key([],"XF86AudioRaiseVolume",lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +2%"),desc="Raises volume"),
    Key([],"XF86AudioMute",lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),desc="Toggles sound"),
    Key([],"XF86MonBrightnessDown",lazy.spawn("brightnessctl -q s 5%-"),desc="Decreases brightness"),
    Key([],"XF86MonBrightnessUp",lazy.spawn("brightnessctl -q s +5%"),desc="Increases brightness"),
    Key([supr, "shift"],"p",lazy.spawn("poweroff"),desc="Shutdown the system"),
    Key([supr, "shift"],"r",lazy.spawn("reboot"),desc="Reboot the system"),
]

for vt in range(1, 8):
    keys.append(Key(["control", "mod1"],f"f{vt}",lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),desc=f"Switch to VT{vt}",))


groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

group_labels=["௧","௨","௩","௪","௫","௬","௭","௮","௯"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            label=group_labels[i],
        ))

for i in groups:
    keys.extend(
        [
            Key([mod],i.name,lazy.group[i.name].toscreen(),desc="Switch to group {}".format(i.name),),
            Key([mod, "shift"],i.name,lazy.window.togroup(i.name, switch_group=True),desc="Switch to & move focused window to group {}".format(i.name),),
        ]
    )


layouts = [
    layout.Columns(border_focus = "#EBDBB2", border_width=4,margin=(10,15,15,15)),
    layout.Max(border_focus = "#EBDBB2", border_width=4,margin=(15,15,15,15)),
    layout.Stack(border_focus = "#EBDBB2", border_width=4,margin=(15,15,15,15),num_stacks=4),
    layout.Tile(border_focus = "#EBDBB2", border_width=4,margin=(15,15,15,15)),
]

widget_defaults = dict(
    font="jetbrains mono nerd font",
    fontsize=19,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/wallpapers/gruv/gruv-desert.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.CurrentLayout(
                   background="#242424",
                   foreground="#000",
                   decorations=[RD('#EBDBB2',5)],
                   padding=15,
                   margin=10,
                   fontsize=15
                ),
                widget.Sep(
                   linewidth = 2,
                   padding = 10,
                   background="#242424",
                   foreground="#242424"
                ), 
                widget.GroupBox(
                   background="#242424",
                   foreground="#EBDBB2",
                   fontsize=22,
                   padding=2,
                   rounded=False,
                   highlight_method="text",
                   active="#EBDBB2",
                   inactive="#32302F",
                   this_current_screen_border = "#EBDBB2"
                ),
                widget.Spacer(
                   background="#242424"
                ),
                widget.TextBox(
                   fmt='twisted 󰙴 ',
                   fontsize=15,
                   background="#242424",
                   foreground="#000",
                   padding=15,
                   decorations=[RD('#EBDBB2',5)]
                ),
                widget.Spacer(
                   background="#242424"
                ),
                widget.Volume(
                   fmt="󰕾 {}",
                   foreground="#000",
                   background="#242424",
                   padding=15,
                   fontsize=15,
                   decorations=[RD('#EBDBB2',5)]
                ),
                widget.Sep(
                   linewidth = 2,
                   padding = 5,
                   background="#242424",
                   foreground="#242424"
                ), 
                widget.Wlan(
                   format=" {essid}",
                   interface="wlp1s0",
                   foreground="#000",
                   background="#242424",
                   fontsize=15,
                   padding=15,
                   decorations=[RD('#EBDBB2',5)]
                ),
                widget.Sep(
                   linewidth = 2,
                   padding = 5,
                   background="#242424",
                   foreground="#242424"
                ), 
                widget.DF(
                   format='{uf}{m} 󰒋 ',
                   visible_on_warn=False,
                   foreground="#000",
                   background="#242424",
                   fontsize=15,
                   padding=15,
                   decorations=[RD('#EBDBB2',5)]
                ),
                widget.Sep(
                   linewidth = 2,
                   padding = 5,
                   background="#242424",
                   foreground="#242424",
                   # foreground="#504945",
                ),   
                widget.UPowerWidget(
                    background = "#242424",
                    foreground = "#000",
                    border_colour = '#000',
                    border_critical_colour = '#fb4934',
                    border_charge_colour = '#b8bb26',
                    decorations=[RD('#EBDBB2',5)],
                    fill_low = '#fe8019',
                    fill_charge = '#b8bb26',
                    fill_critical = '#fb4934',
                    fill_normal = '#000',
                    margin=15,
                    percentage_low = 0.4,
                    percentage_critical = 0.2,
                ),        
                widget.Battery(
                    format="{percent:2.0%}",
                    background="#242424",
                    foreground="#000",
                    low_percentage=0.15,
                    show_short_text=False,
                    decorations=[RD('#EBDBB2',5)],
                    notify_below=10,
                    fontsize=15,
                    padding=10
                ),
                widget.Sep(
                   linewidth = 2,
                   padding = 10,
                   background="#242424",
                   foreground="#242424"
                ), 
                widget.Clock(
                   format="  %H:%M:%S ",
                   background="#242424",
                   foreground="#000",
                   decorations=[RD('#EBDBB2',5)],
                   fontsize=15,
                   padding=10 
                ),
            ],
            size=34,
            border_width=[1, 1, 1, 1],
            border_color=["#000", "#000", "#000", "#000"],
            margin=[10, 15, 0, 15],
        ),
    ),
]

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    border_focus = "#EBDBB2",
    border_width = 4
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wl_xcursor_theme = None
wl_xcursor_size = 24

wmname = "LG3D"

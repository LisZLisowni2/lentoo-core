subarch: amd64
target: livecd-stage1
version_stamp: 1.0
rel_type: default
profile: default/linux/amd64/23.0/desktop
snapshot: 20260313
source_subpath: default/stage3-amd64-latest
update_seed: yes
update_seed_command: --update --deep --newuse @world

livecd/packages:
    - x11-base/xorg-server
    - x11-wm/xfwm4
    - x11-themes/xfce4-themes
    - xfce-base/xfce4-meta
    - net-libs/webkit-gtk
    - net-misc/networkmanager
    - x11-terms/xfce4-terminal
    - app-admin/sudo
    - sys-auth/polkit
    - x11-base/xorg-drivers
    - xfce-base/thunar

livecd/use:
    - gtk
    - xft
    - nls
    - dbus
    - networkmanager
    - glamor      
    - udev
    - icu         
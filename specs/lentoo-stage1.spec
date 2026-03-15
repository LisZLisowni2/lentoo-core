subarch: amd64
target: livecd-stage1
version_stamp: 1.0
snapshot_treeish: 3b1e8b42ffb9185e7cc4cf65d41ac6a8a0b4e977
rel_type: default
profile: default/linux/amd64/23.0/desktop
source_subpath: default/stage3-amd64-openrc-latest
portage_confdir: /var/tmp/catalyst/config/lentoo/portage/
portage_prefix: lentoo

livecd/packages:
    x11-base/xorg-server
    x11-themes/xfwm4-themes
    xfce-base/xfce4-meta
    net-libs/webkit-gtk
    net-misc/networkmanager
    x11-terms/xfce4-terminal
    app-admin/sudo
    sys-auth/polkit
    x11-base/xorg-drivers
    xfce-base/thunar
    sys-kernel/linux-firmware

livecd/use:
    gtk
    gtk3
    xft
    nls
    dbus
    networkmanager
    glamor      
    udev
    icu         
#!/bin/bash

echo "root:lentoo" | chpasswd
echo "127.0.0.1 localhost" > /etc/hosts

useradd -m -G users,wheel,audio,video,cdrom,portage -s /bin/bash lentoo
echo "lentoo:lentoo" | chpasswd
echo "lentoo ALL=(ALL) ALL" >> /etc/sudoers

# rc-update add dbus default
# rc-update add networkmanager default
# rc-update add lightdm default

mkdir -p /etc/lightdm/lightdm.conf.d
echo -e "[Seat:*]\nautologin-user=lentoo\nautologin-user-timeout=0" > /etc/lightdm/lightdm.conf.d/autologin.conf
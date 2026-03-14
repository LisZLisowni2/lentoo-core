#!/bin/bash

echo "root:lentoo" | chpasswd
echo "127.0.0.1 localhost" > /etc/hosts

echo "lentoo:lentoo" | chpasswd

rc-update add dbus default
rc-update add networkmanager default
rc-update add lightdm default
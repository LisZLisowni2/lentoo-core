subarch: amd64
target: livecd-stage2
version_stamp: 1.0
snapshot_treeish: 3b1e8b42ffb9185e7cc4cf65d41ac6a8a0b4e977
rel_type: default
profile: default/linux/amd64/23.0/desktop
source_subpath: default/livecd-stage1-amd64-1.0

boot/kernel: gentoo
boot/kernel/gentoo/sources: sys-kernel/gentoo-sources

livecd/bootargs: gentoo dozfs nomodeset

livecd/iso: lentoo-v1.iso
livecd/volid: LENTOO_2026

livecd/rcadd: dbus|default,NetworkManager|default,lightdm|default  
livecd/root_overlay: /var/tmp/catalyst/root_overlay   
livecd/fsscript: /var/tmp/catalyst/scripts/fsscript.sh 
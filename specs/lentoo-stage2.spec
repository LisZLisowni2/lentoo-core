subarch: amd64
target: livecd-stage2
version_stamp: 20260315T171112Z
snapshot_treeish: 3b1e8b42ffb9185e7cc4cf65d41ac6a8a0b4e977
rel_type: default
profile: default/linux/amd64/23.0/desktop
source_subpath: default/livecd-stage1-amd64-20260315T171112Z
portage_confdir: /var/tmp/catalyst/config/lentoo/portage/
portage_prefix: lentoo

boot/kernel: gentoo

boot/kernel/gentoo/distkernel: yes
boot/kernel/gentoo/dracut_args: --xz --no-hostonly -a dmsquash-live -a dmsquash-live-ntfs -a mdraid -o btrfs -o crypt -o i18n -o usrmount -o lunmask -o qemu -o qemu-net -o nvdimm -o multipath -i /lib/keymaps /lib/keymaps -I busybox
boot/kernel/gentoo/config: /var/tmp/catalyst/config/lentoo/kconfig/amd64/.config
boot/kernel/gentoo/packages: --usepkg n net-wireless/broadcom-sta sys-fs/zfs

livecd/bootargs: nodhcp
livecd/fstype: squashfs
livecd/iso: lentoo-20260315T171112Z.iso
livecd/volid: Lentoo

livecd/rcadd: dbus|default NetworkManager|default display-manager|default gpm|default
livecd/root_overlay: /var/tmp/catalyst/root_overlay/  
livecd/fsscript: /var/tmp/catalyst/scripts/fsscript.sh 

livecd/unmerge:
	app-admin/eselect-ctags
	app-admin/eselect-vi
	app-admin/perl-cleaner
	app-admin/python-updater
	app-portage/gentoolkit
	dev-build/libtool
	dev-libs/gmp
	dev-libs/libxml2
	dev-libs/mpfr
	dev-python/pycrypto
	dev-util/pkgconf
	perl-core/PodParser
	perl-core/Test-Harness
	sys-apps/debianutils
	sys-apps/diffutils
	sys-apps/groff
	sys-apps/miscfiles
	sys-apps/sandbox
	sys-apps/texinfo
	sys-devel/bison
	sys-devel/flex
	sys-devel/gnuconfig
	sys-devel/m4
	sys-libs/db
	sys-libs/gdbm

livecd/empty:
	/boot
	/etc/cron.daily
	/etc/cron.hourly
	/etc/cron.monthly
	/etc/cron.weekly
	/etc/kernel/config.d
	/etc/logrotate.d
	/etc/modules.autoload.d
	/etc/rsync
	/etc/runlevels/single
	/etc/skel
	/root/.ccache
	/tmp
	/usr/include
	/usr/local
	/usr/share/aclocal
	/usr/share/baselayout
	/usr/share/binutils-data
	/usr/share/consolefonts/partialfonts
	/usr/share/consoletrans
	/usr/share/dict
	/usr/share/doc
	/usr/share/emacs
	/usr/share/et
	/usr/share/gcc-data
	/usr/share/gettext
	/usr/share/glib-2.0
	/usr/share/gnuconfig
	/usr/share/gtk-doc
	/usr/share/i18n
	/usr/share/info
	/usr/share/lcms
	/usr/share/libtool
	/usr/share/man
	/usr/share/rfc
	/usr/share/ss
	/usr/share/state
	/usr/share/texinfo
	/usr/share/unimaps
	/usr/share/zoneinfo
	/usr/src
	/var/cache
	/var/empty
	/var/lib/portage
	/var/log
	/var/spool
	/var/state
	/var/tmp

livecd/rm:
	/etc/*-
	/etc/*.old
	/etc/default/audioctl
	/etc/dispatch-conf.conf
	/etc/etc-update.conf
	/etc/hosts.bck
	/etc/issue*
	/etc/man.conf
	/etc/resolv.conf
	/root/.bash_history
	/root/.viminfo
	/usr/bin/*.static
	/usr/bin/fsck.cramfs
	/usr/bin/fsck.minix
	/usr/bin/mkfs.bfs
	/usr/bin/mkfs.cramfs
	/usr/bin/mkfs.minix
	/usr/bin/addr2line
	/usr/share/consolefonts/1*
	/usr/share/consolefonts/7*
	/usr/share/consolefonts/8*
	/usr/share/consolefonts/9*
	/usr/share/consolefonts/A*
	/usr/share/consolefonts/C*
	/usr/share/consolefonts/E*
	/usr/share/consolefonts/G*
	/usr/share/consolefonts/L*
	/usr/share/consolefonts/M*
	/usr/share/consolefonts/R*
	/usr/share/consolefonts/a*
	/usr/share/consolefonts/c*
	/usr/share/consolefonts/dr*
	/usr/share/consolefonts/g*
	/usr/share/consolefonts/i*
	/usr/share/consolefonts/k*
	/usr/share/consolefonts/l*
	/usr/share/consolefonts/r*
	/usr/share/consolefonts/s*
	/usr/share/consolefonts/t*
	/usr/share/consolefonts/v*
	/usr/share/misc/*.old

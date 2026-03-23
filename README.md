![](assets/LogoLentooSmall.png)

# Lentoo Linux

**Lentoo** is a distribution based on Gentoo, created to provide a more user-friendly experience for users who value source compilation but seek a modern and user-friendly interface.

> **Project status:** Pre-alpha.

## Project goals
Main goal of Lentoo is to lower the barrier to entry into the world of Gentoo without sacrificing its flexibility. Planned functions are:
* **Lentoo Installer:** Graphical Installer based on Tauri
* **Lentoo Manager:** User-friendly GUI to manage packages and USE flags, license and environment per package
* **EasyConfigMake:** Tool to graphical configuration of `make.conf`, accept keywords and masks.
* **Lightweight:** Default desktop environment is Xfce which provides perfomance and ease of use.

## System building
Project use official tool **Catalyst** to generate LiveCD images. Configurations are located in `specs/`.

### How to build test image?
To generate stage1 image, make sure you have `dev-util/catalyst` installed and run:

```bash
# Generate tmp directory for catalyst
sudo mkdir -p /var/tmp/catalyst/builds/default

# Download seed file
wget https://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64/stage3-openrc-amd64-YYYYMMDDTHHMMSSZ.tar.xz -O /var/tmp/catalyst/builds/default/stage3-amd64-openrc-latest.tar.xz

# Generate snapshot
catalyst --snapshot stable # This will generate a commit hash, remember to change it in *.spec files

# Prepare stages
sudo ./scripts/prepare-stages.sh

# Build stage1 image
sudo catalyst -f specs/stage1.spec

# Build stage2 iso
sudo catalyst -f specs/stage2.spec
```

## License

Project Lentoo is available on GNU General Public License v3.0 (GPL-3.0).

> Lentoo is an independent fork and is not officially supported by the Gentoo Foundation.
> Gentoo is a registered trademark of Gentoo Foundation, Inc.

Compile with patience, use with joy.

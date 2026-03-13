# Lentoo Linux

**Lentoo** is a distribution based on Gentoo, created to provide a more user-friendly experience for users who value source compilation but seek a modern and user-friendly interface.

> **Project status:** Pre-alpha.

## Project goals
Main goal of Lentoo is to lower the barrier to entry into the world of Gentoo without sacrificing its flexibility. Planned functions are:
* **Lentoo Installer:** Graphical Installer based on Tauri
* **Lentoo Manager:** User-friendly GUI to manage packages and USE flags
* **EasyConfig:** Tool to graphical configuration of `make.conf`.
* **Lekkość:** Default desktop environment is Xfce which provides perfomance and ease of use.

## System building
Project use official tool **Catalyst** to generate LiveCD images. Configurations are located in `specs/`.

### How to build test image?
To generate stage1 image, make sure you have `dev-util/catalyst` installed and run:

```bash
sudo catalyst -f specs/stage1.spec
```

## License

Project Lentoo is available on GNU General Public License v3.0 (GPL-3.0).

> Lentoo is an independent fork and is not officially supported by the Gentoo Foundation.
> Gentoo is a registered trademark of Gentoo Foundation, Inc.

Compile with patience, use with joy.

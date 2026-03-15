#!/bin/bash

ROOT_PROJECT=$(cd "$(dirname $BASH_SOURCES[0]})" && pwd)
CATALYST_TMP_DIR="/var/tmp/catalyst"
CATALYST_CONF_DIR="$CATALYST_TMP_DIR/config"

echo ">>> Preparing stage1 environment"

echo ">> Copying portage configuration to catalyst temporary directory"
rm -rf "$CATALYST_CONF_DIR"
mkdir -p "$CATALYST_CONF_DIR"
cp -r "$ROOT_PROJECT/releases/." "$CATALYST_CONF_DIR/lentoo/"

echo ">> Setting up make.conf"
echo "MAKEOPTS=\"-j$(nproc) -l$(nproc)\"" >> "$CATALYST_CONF_DIR/lentoo/portage/make.conf"
echo "EMERGE_DEFAULT_OPTS=\"--jobs=$(nproc) --load-average=$(nproc) --with-bdeps=y --binpkg-respect-use=y --usepkg --quiet\"" >> "$CATALYST_CONF_DIR/lentoo/portage/make.conf"
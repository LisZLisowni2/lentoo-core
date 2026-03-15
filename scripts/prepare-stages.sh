#!/bin/bash

ROOT_PROJECT=$(cd "$(dirname $BASH_SOURCES[0]})" && pwd)
CATALYST_TMP_DIR="/var/tmp/catalyst"
CATALYST_CONF_DIR="$CATALYST_TMP_DIR/config"
CATALYST_SCRIPTS_DIR="$CATALYST_TMP_DIR/scripts"
CATALYST_ROOT_OVERLAY="$CATALYST_TMP_DIR/root_overlay"
CATALYST_KERNEL_CONF="$CATALYST_TMP_DIR/kernel_config"

echo ">>> Preparing stage1 environment"

echo ">> Copying portage configuration to catalyst temporary directory"
rm -rf "$CATALYST_CONF_DIR"
mkdir -p "$CATALYST_CONF_DIR"
cp -r "$ROOT_PROJECT/releases/." "$CATALYST_CONF_DIR/lentoo/"

echo ">>> Preparing stage2 environment"

echo ">> Copying scripts to catalyst temporary directory"
rm -rf "$CATALYST_SCRIPTS_DIR"
mkdir -p "$CATALYST_SCRIPTS_DIR"
cp -r "$ROOT_PROJECT/scripts/." "$CATALYST_SCRIPTS_DIR/"

echo ">> Copying root overlay to catalyst temporary directory"
rm -rf "$CATALYST_ROOT_OVERLAY"
mkdir -p "$CATALYST_ROOT_OVERLAY"
cp -r "$ROOT_PROJECT/root_overlay/." "$CATALYST_ROOT_OVERLAY/"
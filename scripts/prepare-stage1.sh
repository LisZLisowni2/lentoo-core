#!/bin/bash

ROOT_PROJECT=$(cd "$(dirname $BASH_SOURCES[0]})" && pwd)
CATALYST_TMP_DIR="/var/tmp/catalyst"
CATALYST_CONF_DIR="$CATALYST_TMP_DIR/lentoo-config"

echo ">>> Preparing stage1 environment"
echo "$CATALYST_CONF_DIR"

rm -rf "$CATALYST_CONF_DIR"
mkdir -p "$CATALYST_CONF_DIR"
cp -r "$ROOT_PROJECT/releases/." "$CATALYST_CONF_DIR/"
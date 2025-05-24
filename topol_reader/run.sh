#!/bin/bash
set -e

echo "Starting Topol Reader..."

while true; do
    python3 -u /app/main.py
    echo "Sleeping..."
    sleep $HASSIO_ADDON_OPTIONS_INTERVAL
done

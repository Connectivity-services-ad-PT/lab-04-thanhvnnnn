#!/usr/bin/env bash
set -euo pipefail
prism mock contracts/notification.openapi.yaml --host 0.0.0.0 --port 4010

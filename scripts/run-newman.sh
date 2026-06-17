#!/usr/bin/env bash
set -euo pipefail
mkdir -p reports
newman run postman/collections/FIT4110_lab04_notification_docker.postman_collection.json -e postman/environments/FIT4110_lab04_local.postman_environment.json -r cli,junit,htmlextra

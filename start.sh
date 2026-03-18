#!/bin/bash
set -e
echo "Starting IoT-Powered Smart Home Dashboard..."
uvicorn app:app --host 0.0.0.0 --port 9026 --workers 1

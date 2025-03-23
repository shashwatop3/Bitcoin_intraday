#!/bin/bash
# Start cron in the background
cron
# Start uvicorn
uvicorn backend.server:app --host 0.0.0.0 --port 8000

#!/bin/bash

# Usage: ./log_cpu_mem.sh <PID> <duration_in_seconds>

PID=$1
DURATION=$2
OUTPUT_FILE="cpu_mem_log_${PID}.csv"

if [ -z "$PID" ] || [ -z "$DURATION" ]; then
  echo "Usage: $0 <PID> <duration_in_seconds>"
  exit 1
fi

echo "Timestamp,CPU_Usage(%),Memory_Usage(%),ElapsedTime" > "$OUTPUT_FILE"

echo "Logging CPU and memory usage for PID $PID for $DURATION seconds..."
for ((i=0; i<$DURATION; i++)); do
  TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
  STATS=$(ps -p $PID -o %cpu,%mem,etime= | awk '{print $1","$2","$3}')
  if [ -n "$STATS" ]; then
    echo "$TIMESTAMP,$STATS" >> "$OUTPUT_FILE"
  else
    echo "$TIMESTAMP,Process not found" >> "$OUTPUT_FILE"
    break
  fi
  sleep 1
done

echo "Logging complete. Output saved to $OUTPUT_FILE"

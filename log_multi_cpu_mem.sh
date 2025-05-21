#!/bin/bash

# Usage: ./log_multi_cpu_mem.sh "<PID1> <PID2> ..." <duration_in_seconds>

PIDS=($1)
DURATION=$2
OUTPUT_FILE="cpu_mem_log_multi.csv"

if [ -z "$PIDS" ] || [ -z "$DURATION" ]; then
  echo "Usage: $0 \"<PID1> <PID2> ...\" <duration_in_seconds>"
  exit 1
fi

echo "Timestamp,PID,CPU_Usage(%),Memory_Usage(%),ElapsedTime" > "$OUTPUT_FILE"

echo "Logging CPU and memory usage for PIDs: ${PIDS[@]} for $DURATION seconds..."
for ((i=0; i<$DURATION; i++)); do
  TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
  for PID in "${PIDS[@]}"; do
    STATS=$(ps -p $PID -o %cpu,%mem,etime= | awk 'NR==2 {print $1","$2","$3}')
    if [ -n "$STATS" ]; then
      echo "$TIMESTAMP,$PID,$STATS" >> "$OUTPUT_FILE"
    else
      echo "$TIMESTAMP,$PID,Process not found" >> "$OUTPUT_FILE"
    fi
  done
  sleep 1
done

echo "Logging complete. Output saved to $OUTPUT_FILE"

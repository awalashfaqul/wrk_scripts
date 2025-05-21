#!/bin/bash

# Usage: ./log_avg_cpu_mem_mac.sh "71449 4326" 30
PIDS=($1)
DURATION=$2
OUTPUT_FILE="avg_cpu_mem_summary.csv"

if [ -z "$PIDS" ] || [ -z "$DURATION" ]; then
  echo "Usage: $0 \"<PID1> <PID2>\" <duration_in_seconds>"
  exit 1
fi

echo "PID,CPU_Avg_Percent,Memory_Avg_Percent" > "$OUTPUT_FILE"

for PID in "${PIDS[@]}"; do
  CPU_TOTAL=0
  MEM_TOTAL=0
  COUNT=0

  for ((i=0; i<$DURATION; i++)); do
    # Use ps -p <pid> -o %cpu,%mem (macOS-compatible)
    STATS=$(ps -p $PID -o %cpu,%mem | tail -n 1 | awk '{print $1","$2}')
    if [ -n "$STATS" ]; then
      CPU=$(echo "$STATS" | cut -d',' -f1)
      MEM=$(echo "$STATS" | cut -d',' -f2)
      CPU_TOTAL=$(echo "$CPU_TOTAL + $CPU" | bc)
      MEM_TOTAL=$(echo "$MEM_TOTAL + $MEM" | bc)
      ((COUNT++))
    fi
    sleep 1
  done

  if [ "$COUNT" -gt 0 ]; then
    CPU_AVG=$(echo "scale=2; $CPU_TOTAL / $COUNT" | bc)
    MEM_AVG=$(echo "scale=2; $MEM_TOTAL / $COUNT" | bc)
    echo "$PID,$CPU_AVG,$MEM_AVG" >> "$OUTPUT_FILE"
  fi
done

echo "Logging complete. Output saved to $OUTPUT_FILE"

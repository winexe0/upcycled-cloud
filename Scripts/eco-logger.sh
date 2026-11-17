#!/bin/bash
# Eco-Logger for Android Benchmarking
OUTPUT="energy_log_$(date +%s).csv"
echo "Timestamp,Voltage_uV,Current_uA,Temp_C,Battery_Pct" > $OUTPUT

echo "Starting logging... Press Ctrl+C to stop."

while true; do
    # Read Kernel Nodes
    VOLT=$(cat /sys/class/power_supply/battery/voltage_now 2>/dev/null || echo 0)
    CURR=$(cat /sys/class/power_supply/battery/current_now 2>/dev/null || echo 0)
    TEMP=$(cat /sys/class/power_supply/battery/temp 2>/dev/null || echo 0)
    CAP=$(cat /sys/class/power_supply/battery/capacity 2>/dev/null || echo 0)
    TS=$(date +%s)

    # Log to file
    echo "$TS,$VOLT,$CURR,$TEMP,$CAP" >> $OUTPUT
    
    # 1000ms polling rate
    sleep 1
done


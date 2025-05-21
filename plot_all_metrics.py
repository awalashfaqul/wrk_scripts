import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("results.csv")

# Metrics to plot
metrics = {
    "RequestsPerSec": ("Average Requests/sec", "Requests/sec", ['skyblue', 'lightgreen']),
    "AvgLatencyMs": ("Average Latency", "Latency (ms)", ['salmon', 'orange']),
    "MaxLatencyMs": ("Max Latency", "Latency (ms)", ['plum', 'lightcoral']),
    "StdevMs": ("Latency Standard Deviation", "Std Dev (ms)", ['lightblue', 'gold']),
    "PlusMinusStdevPercent": ("+/- Std Dev", "Percentage (%)", ['lightgray', 'lightpink']),
    "TransferPerSecMB": ("Transfer/sec", "MB/sec", ['lightseagreen', 'khaki'])
}

# Plot each metric
for metric, (title, ylabel, colors) in metrics.items():
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Bar Chart
    axs[0].bar(df['Framework'], df[metric], color=colors)
    axs[0].set_title(f"{title} (Bar Chart)")
    axs[0].set_ylabel(ylabel)
    axs[0].grid(axis='y')

    # Pie Chart
    axs[1].pie(df[metric], labels=df['Framework'], autopct='%1.1f%%', colors=colors)
    axs[1].set_title(f"{title} (Pie Chart)")

    plt.tight_layout()
    filename = metric.lower() + "_combined.png"
    plt.savefig(filename)
    plt.show()

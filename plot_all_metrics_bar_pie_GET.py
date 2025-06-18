import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("results_get.csv")

# Define metrics: column name, chart title, y-axis label, and colors
metrics = {
    "LatencyAvgMs": ("Average Latency", "Latency (ms)", ['salmon', 'orange']),
    "ReqPerSecAvg": ("Average Requests/sec", "Requests/sec", ['skyblue', 'lightgreen']),
    "TransferPerSecMB": ("Transfer/sec", "MB/sec", ['lightseagreen', 'mediumaquamarine'])
}

# Set up subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("GET Performance Comparison: .NET vs Phoenix", fontsize=18)

# Generate bar charts for each metric
for idx, (metric, (title, ylabel, colors)) in enumerate(metrics.items()):
    axs[idx].bar(df['Framework'], df[metric], color=colors)
    axs[idx].set_title(title)
    axs[idx].set_ylabel(ylabel)
    axs[idx].set_ylim(0, df[metric].max() * 1.2)  # add some space on top of bars

# Adjust layout and save figure
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("get_endpoint_performance_bar_charts.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("results_put.csv")

# Metrics to plot
metrics = {
    "LatencyAvgMs": ("Average Latency", "Latency (ms)", ['salmon', 'orange']),
    "ReqPerSecAvg": ("Average Requests/sec", "Requests/sec", ['skyblue', 'lightgreen']),
    "TransferPerSecMB": ("Transfer/sec", "MB/sec", ['lightseagreen', 'mediumaquamarine'])
}

# Create subplots (1 row, 3 columns)
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("PUT Performance Comparison: .NET vs Phoenix", fontsize=18)

# Iterate over metrics and draw bar charts
for idx, (metric, (title, ylabel, colors)) in enumerate(metrics.items()):
    axs[idx].bar(df['Framework'], df[metric], color=colors)
    axs[idx].set_title(title)
    axs[idx].set_ylabel(ylabel)
    axs[idx].set_ylim(0, df[metric].max() * 1.2)  # Add some padding above bars

# Final layout adjustment
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("put_bar_comparison.png")
plt.show()

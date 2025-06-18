import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("results_delete.csv")

# Metrics to plot
metrics = {
    "LatencyAvgMs": ("Average Latency", "Latency (ms)", ['salmon', 'orange']),
    "ReqPerSecAvg": ("Average Requests/sec", "Requests/sec", ['skyblue', 'lightgreen']),
    "TransferPerSecMB": ("Transfer/sec", "MB/sec", ['lightseagreen', 'mediumaquamarine'])
}

# Create 1 row with 3 bar charts
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("DELETE Performance Comparison: .NET vs Phoenix", fontsize=18)

for i, (metric, (title, ylabel, colors)) in enumerate(metrics.items()):
    axs[i].bar(df['Framework'], df[metric], color=colors)
    axs[i].set_title(title, fontsize=14)
    axs[i].set_ylabel(ylabel)
    axs[i].set_ylim(0, df[metric].max() * 1.2)  # Add some space above max value

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("delete_bar_comparison.png")
plt.show()

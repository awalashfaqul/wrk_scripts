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

# Create 1 row with 3 pie charts
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("DELETE Performance Comparison: .NET vs Phoenix", fontsize=18)

for i, (metric, (title, ylabel, colors)) in enumerate(metrics.items()):
    values = df[metric]
    axs[i].pie(values, labels=df['Framework'], autopct='%1.1f%%', colors=colors)
    axs[i].set_title(f"{title}", fontsize=14)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("delete_pie_comparison.png")
plt.show()

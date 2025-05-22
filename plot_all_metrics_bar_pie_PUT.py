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

# Iterate over metrics and draw pie charts
for idx, (metric, (title, ylabel, colors)) in enumerate(metrics.items()):
    values = df[metric]
    axs[idx].pie(values, labels=df['Framework'], autopct='%1.1f%%', colors=colors, startangle=140)
    axs[idx].set_title(title)

# Final layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("put_pie_comparison.png")
plt.show()

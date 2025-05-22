import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("results_get.csv")

# Define metrics: column name, chart title, unit label, and colors
metrics = {
    "LatencyAvgMs": ("Average Latency", "Latency (ms)", ['salmon', 'orange']),
    "ReqPerSecAvg": ("Average Requests/sec", "Requests/sec", ['skyblue', 'lightgreen']),
    "TransferPerSecMB": ("Transfer/sec", "MB/sec", ['lightseagreen', 'mediumaquamarine'])
}

# Set up subplots
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("GET Performance Comparison: .NET vs Phoenix", fontsize=18)

# Generate pie charts for each metric
for idx, (metric, (title, ylabel, colors)) in enumerate(metrics.items()):
    values = df[metric]
    labels = df['Framework']
    axs[idx].pie(values, labels=labels, autopct='%1.1f%%', colors=colors)
    axs[idx].set_title(title)

# Save and show
plt.tight_layout()
plt.savefig("get_endpoint_performance_pie_charts.png")
plt.show()

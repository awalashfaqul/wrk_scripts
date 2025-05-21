import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("results_post.csv")

# Define metrics to visualize
metrics = [
    ("LatencyAvgMs", "Average Latency", "Latency (ms)"),
    ("LatencyStdevMs", "Latency Std Dev", "Std Dev (ms)"),
    ("LatencyMaxMs", "Max Latency", "Latency (ms)"),
    ("LatencyPlusMinusStdevPercent", "Latency +/- Std Dev", "Percent (%)"),
    ("ReqPerSecAvg", "Average Requests/sec", "Requests/sec"),
    ("ReqPerSecStdev", "Requests/sec Std Dev", "Std Dev"),
    ("ReqPerSecMax", "Max Requests/sec", "Requests/sec"),
    ("ReqPerSecPlusMinusStdevPercent", "Requests/sec +/- Std Dev", "Percent (%)"),
    ("TransferPerSecMB", "Transfer/sec", "MB/sec")
]

colors = ['lightcoral', 'lightblue']

# Create dashboard figure
rows = 5
cols = 2
fig, axs = plt.subplots(rows, cols, figsize=(16, 20))
fig.suptitle("POST Performance Comparison: .NET vs Phoenix", fontsize=20)

# Plot each metric as bar and pie chart
for i, (metric, title, ylabel) in enumerate(metrics):
    row, col = divmod(i, 2)

    # Bar chart
    ax_bar = axs[row, col]
    ax_bar.bar(df['Framework'], df[metric], color=colors)
    ax_bar.set_title(f"{title} (Bar)", fontsize=12)
    ax_bar.set_ylabel(ylabel)
    ax_bar.grid(axis='y')

# Hide any extra subplots (if metrics < rows * cols)
total_subplots = rows * cols
if len(metrics) < total_subplots:
    for j in range(len(metrics), total_subplots):
        row, col = divmod(j, cols)
        axs[row, col].axis('off')

plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.savefig("post_performance_dashboard.png")
plt.show()

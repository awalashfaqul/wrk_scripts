import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("results_post.csv")

# Define metrics to plot
metrics = {
    "LatencyAvgMs": ("Average Latency", "Latency (ms)", ['salmon', 'orange']),
    "ReqPerSecAvg": ("Average Requests/sec", "Requests/sec", ['skyblue', 'lightgreen']),
    "TransferPerSecMB": ("Transfer/sec", "MB/sec", ['lightseagreen', 'mediumaquamarine'])
}

# Create one figure with 3 bar charts
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("POST Performance Comparison (.NET vs Phoenix)", fontsize=20)

# Loop through each metric and axis, plot bar charts
for ax, (metric, (title, ylabel, colors)) in zip(axs, metrics.items()):
    ax.bar(df['Framework'], df[metric], color=colors)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_ylim(0, df[metric].max() * 1.2)  # Add some padding above bars

# Layout and save
plt.tight_layout(rect=[0, 0, 1, 0.93])  # Adjust for the suptitle
plt.savefig("post_comparison_barcharts.png")
plt.show()

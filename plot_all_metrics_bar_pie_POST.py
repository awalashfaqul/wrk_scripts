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

# Create one figure with 3 pie charts
fig, axs = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle("POST Performance Comparison (.NET vs Phoenix)", fontsize=20)

# Loop through each metric and corresponding axis
for ax, (metric, (title, ylabel, colors)) in zip(axs, metrics.items()):
    values = df[metric]
    labels = df['Framework']
    ax.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax.set_title(title)

# Layout and save
plt.tight_layout(rect=[0, 0, 1, 0.93])  # Adjust for the suptitle
plt.savefig("post_comparison_piecharts.png")
plt.show()

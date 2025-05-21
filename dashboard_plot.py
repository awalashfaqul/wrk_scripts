import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("results.csv")

# Define metrics
metrics = [
    ("RequestsPerSec", "Average Requests/sec", "Requests/sec"),
    ("AvgLatencyMs", "Average Latency", "Latency (ms)"),
    ("MaxLatencyMs", "Max Latency", "Latency (ms)"),
    ("StdevMs", "Latency Std Dev", "Std Dev (ms)"),
    ("PlusMinusStdevPercent", "+/- Std Dev", "Percent (%)"),
    ("TransferPerSecMB", "Transfer/sec", "MB/sec")
]

colors = ['lightcoral', 'lightblue']

# Create dashboard figure
fig, axs = plt.subplots(3, 4, figsize=(18, 12))
fig.suptitle("Performance Comparison: .NET vs Phoenix", fontsize=20)

for i, (metric, title, ylabel) in enumerate(metrics):
    row, col = divmod(i, 2)

    # Bar chart
    ax_bar = axs[row, col * 2]
    ax_bar.bar(df['Framework'], df[metric], color=colors)
    ax_bar.set_title(title + " (Bar)", fontsize=10)
    ax_bar.set_ylabel(ylabel)
    ax_bar.grid(axis='y')

    # Pie chart
    ax_pie = axs[row, col * 2 + 1]
    ax_pie.pie(df[metric], labels=df['Framework'], autopct='%1.1f%%', colors=colors)
    ax_pie.set_title(title + " (Pie)", fontsize=10)

# Hide unused subplots (if any)
for j in range(6, 12):
    row, col = divmod(j, 4)
    axs[row, col].axis('off')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig("performance_dashboard.png")
plt.show()

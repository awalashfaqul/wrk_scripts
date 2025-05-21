import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("results_post.csv")

# Metrics and plot settings
metrics = {
    "LatencyAvgMs": ("Average Latency", "Latency (ms)", ['salmon', 'orange']),
    "LatencyStdevMs": ("Latency Std Dev", "Std Dev (ms)", ['lightblue', 'gold']),
    "LatencyMaxMs": ("Max Latency", "Latency (ms)", ['plum', 'lightcoral']),
    "LatencyPlusMinusStdevPercent": ("Latency +/- Std Dev", "Percent (%)", ['lightgray', 'lightpink']),
    "ReqPerSecAvg": ("Average Requests/sec", "Requests/sec", ['skyblue', 'lightgreen']),
    "ReqPerSecStdev": ("Requests/sec Std Dev", "Std Dev", ['lightskyblue', 'khaki']),
    "ReqPerSecMax": ("Max Requests/sec", "Requests/sec", ['orchid', 'lightcyan']),
    "ReqPerSecPlusMinusStdevPercent": ("Requests/sec +/- Std Dev", "Percent (%)", ['lightyellow', 'tomato']),
    "TransferPerSecMB": ("Transfer/sec", "MB/sec", ['lightseagreen', 'mediumaquamarine'])
}

frameworks = df['Framework']
num_metrics = len(metrics)

# === BAR CHART SUMMARY ===
fig_bar, axs_bar = plt.subplots(nrows=(num_metrics + 1) // 2, ncols=2, figsize=(14, num_metrics * 2.5))
axs_bar = axs_bar.flatten()

# === PIE CHART SUMMARY ===
fig_pie, axs_pie = plt.subplots(nrows=(num_metrics + 1) // 2, ncols=2, figsize=(14, num_metrics * 2.5))
axs_pie = axs_pie.flatten()

# Plot each metric into summary figures
for i, (metric, (title, ylabel, colors)) in enumerate(metrics.items()):
    values = df[metric]

    # Bar chart subplot
    axs_bar[i].bar(frameworks, values, color=colors)
    axs_bar[i].set_title(title)
    axs_bar[i].set_ylabel(ylabel)
    axs_bar[i].grid(axis='y')

    # Pie chart subplot
    axs_pie[i].pie(values, labels=frameworks, autopct='%1.1f%%', colors=colors)
    axs_pie[i].set_title(title)

# Remove any unused subplots
for j in range(i+1, len(axs_bar)):
    fig_bar.delaxes(axs_bar[j])
    fig_pie.delaxes(axs_pie[j])

# Final layout & save
fig_bar.tight_layout()
fig_bar.savefig("summary_bar_charts.png")
fig_bar.show()

fig_pie.tight_layout()
fig_pie.savefig("summary_pie_charts.png")
fig_pie.show()

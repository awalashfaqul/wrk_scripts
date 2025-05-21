import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("results_post.csv")

# Metrics to plot
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

# Plot each metric: Bar, Pie
for metric, (title, ylabel, colors) in metrics.items():
    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle("CRUD (POST) Performance Comparison: .NET vs Phoenix", fontsize=20)
    frameworks = df['Framework']
    values = df[metric]

    # Bar Chart
    axs[0].bar(frameworks, values, color=colors)
    axs[0].set_title(f"{title} (Bar Chart)")
    axs[0].set_ylabel(ylabel)
    axs[0].grid(axis='y')

    # Pie Chart
    axs[1].pie(values, labels=frameworks, autopct='%1.1f%%', colors=colors)
    axs[1].set_title(f"{title} (Pie Chart)")


    # Layout & Save
    plt.tight_layout()
    filename = metric.lower() + "_charts.png"
    plt.savefig(filename)
    plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("avg_cpu_mem_summary.csv")

# Label mapping (optional)
pid_to_label = {
    71449: ".NET (71449)",
    4326: "Phoenix (4326)"
}
df["Label"] = df["PID"].map(pid_to_label)

# Plotting
def plot_metric(metric, title, ylabel, colors):
    values = df[metric]
    labels = df["Label"]

    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    # Bar chart
    axs[0].bar(labels, values, color=colors)
    axs[0].set_title(f"{title} (Bar Chart)")
    axs[0].set_ylabel(ylabel)
    axs[0].grid(axis='y')

    # Pie chart
    axs[1].pie(values, labels=labels, autopct='%1.1f%%', colors=colors)
    axs[1].set_title(f"{title} (Pie Chart)")

    plt.tight_layout()
    plt.savefig(f"{metric.lower()}_usage.png")
    plt.show()

# Plot both metrics
plot_metric("CPU_Avg_Percent", "Average CPU Usage over 30s", "CPU Usage (%)", ['steelblue', 'lightgreen'])
plot_metric("Memory_Avg_Percent", "Average Memory Usage over 30s", "Memory Usage (%)", ['salmon', 'gold'])

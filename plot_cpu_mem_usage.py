import pandas as pd
import matplotlib.pyplot as plt

# Load CSV log file
df = pd.read_csv("cpu_mem_log_multi.csv")

# Filter out rows with missing data or 'Process not found'
df = df[df['CPU_Usage(%)'].apply(lambda x: str(x).replace('.', '', 1).isdigit())]

# Convert CPU and Memory usage columns to float
df['CPU_Usage(%)'] = df['CPU_Usage(%)'].astype(float)
df['Memory_Usage(%)'] = df['Memory_Usage(%)'].astype(float)

# Map PIDs to framework names
pid_map = {71449: '.NET', 4326: 'Phoenix'}
df['Framework'] = df['PID'].map(pid_map)

# Group by framework and calculate average CPU and memory usage
avg_usage = df.groupby('Framework')[['CPU_Usage(%)', 'Memory_Usage(%)']].mean()

# Bar and Pie plot function
def plot_metric(metric, ylabel, colors):
    fig, axs = plt.subplots(1, 2, figsize=(12,5))

    # Bar chart
    axs[0].bar(avg_usage.index, avg_usage[metric], color=colors)
    axs[0].set_title(f'Average {ylabel} by Framework')
    axs[0].set_ylabel(ylabel)
    axs[0].grid(axis='y')

    # Pie chart
    axs[1].pie(avg_usage[metric], labels=avg_usage.index, autopct='%1.1f%%', colors=colors)
    axs[1].set_title(f'{ylabel} Distribution')

    plt.tight_layout()
    plt.show()

# Colors for .NET and Phoenix
colors = ['deepskyblue', 'coral']

# Plot Average CPU Usage (%)
plot_metric('CPU_Usage(%)', 'CPU Usage (%)', colors)

# Plot Average Memory Usage (%)
plot_metric('Memory_Usage(%)', 'Memory Usage (%)', colors)

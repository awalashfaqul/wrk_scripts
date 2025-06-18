import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("performance_data.csv")

# Split into two dataframes
latency_df = df[df['Metric'].str.contains('Latency')].copy()
rps_df = df[df['Metric'].str.contains('Requests/sec')].copy()

# Set plot style
plt.style.use('ggplot')

# -----------------------------
# Avg Latency Bar Chart
# -----------------------------
fig, ax1 = plt.subplots(figsize=(10, 6))
x = latency_df['Operation']
width = 0.35
x_indexes = range(len(x))

ax1.bar([i - width/2 for i in x_indexes], latency_df['EF Core (.NET)'], width=width, label=".NET", color='salmon')
ax1.bar([i + width/2 for i in x_indexes], latency_df['Ecto (Phoenix)'], width=width, label="Phoenix", color='blue')

ax1.set_title("Average Latency per Operation")
ax1.set_ylabel("Latency (ms)")
ax1.set_xticks(list(x_indexes))
ax1.set_xticklabels(x)
ax1.legend()
plt.tight_layout()
plt.savefig("avg_latency_comparison.png")
plt.show()

# -----------------------------
# Avg Requests/sec Bar Chart
# -----------------------------
fig, ax2 = plt.subplots(figsize=(10, 6))
x = rps_df['Operation']
x_indexes = range(len(x))

ax2.bar([i - width/2 for i in x_indexes], rps_df['EF Core (.NET)'], width=width, label=".NET", color='green')
ax2.bar([i + width/2 for i in x_indexes], rps_df['Ecto (Phoenix)'], width=width, label="Phoenix", color='orange')

ax2.set_title("Average Requests/sec per Operation")
ax2.set_ylabel("Requests/sec")
ax2.set_xticks(list(x_indexes))
ax2.set_xticklabels(x)
ax2.legend()
plt.tight_layout()
plt.savefig("avg_requests_per_sec_comparison.png")
plt.show()

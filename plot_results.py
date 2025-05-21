import pandas as pd
import matplotlib.pyplot as plt

# Load results
df = pd.read_csv("results.csv")

# Plot 1: Average Requests per Second
plt.figure(figsize=(8, 5))
plt.bar(df['Framework'], df['AvgRequestsPerSec'], color=['skyblue', 'lightgreen'])
plt.title("Average Requests per Second: .NET vs Phoenix")
plt.ylabel("Requests/sec")
plt.xlabel("Framework")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

# Plot 2: Average Latency
plt.figure(figsize=(8, 5))
plt.bar(df['Framework'], df['AvgLatencyMs'], color=['salmon', 'orange'])
plt.title("Average Latency (us): .NET vs Phoenix")
plt.ylabel("Latency (us)")
plt.xlabel("Framework")
plt.grid(axis='y')
plt.tight_layout()
plt.show()

plt.savefig("throughput_comparison.png")
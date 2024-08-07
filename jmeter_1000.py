import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['standalone', 'single-node', 'three-node']
plus_values = [0, 43, 48]  # Values for the '+' column
minus_values = [24, 29, 35]  # Values for the '-' column

# Number of categories
n = len(categories)

# Create an array with the position of each bar along the x-axis
x = np.arange(n)

# Width of the bars
width = 0.35

# Create the figure and the axes
fig, ax = plt.subplots(figsize=(10, 6))  # Increased figure size for better readability

# Plot the bars
bars1 = ax.bar(x - width/2, plus_values, width, label='transaction', edgecolor='black')
bars2 = ax.bar(x + width/2, minus_values, width, label='non-transaction', edgecolor='black')

# Add exact values above the bars
for bar in bars1:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,  # x position
        height + 1,  # y position (slightly above the bar)
        f'{height}',  # Value to display
        ha='center',  # Horizontal alignment
        va='bottom'  # Vertical alignment
    )

for bar in bars2:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,  # x position
        height + 1,  # y position (slightly above the bar)
        f'{height}',  # Value to display
        ha='center',  # Horizontal alignment
        va='bottom'  # Vertical alignment
    )

# Add labels, title, and legend
ax.set_xlabel('Configuration')
ax.set_ylabel('Time (ms)')
ax.set_title('JMeter Benchmark - 1000 Requests')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')  # Rotate labels for better readability
ax.legend()

# Optionally, add a grid
ax.yaxis.grid(True)

# Save the plot
plt.savefig('histogram/jmeter_1000_requests.png')

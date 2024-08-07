import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['(w:0, j:false)', '(w:1, j:false)', '(w:0, j:true)', '(w:1, j:true)', '(w:majority)']
values = [0.186, 1.754, 0, 10.548, 9.291]  # Single set of double values

# Number of categories
n = len(categories)

# Create an array with the position of each bar along the x-axis
x = np.arange(n)

# Width of the bars
width = 0.4

# Create the figure and the axes
fig, ax = plt.subplots(figsize=(10, 6))  # Increased figure size for better readability

# Plot the bars
bars = ax.bar(x, values, width, edgecolor='black')

# Add exact values above the bars
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,  # x position
        height + 0.5,  # y position (slightly above the bar)
        f'{height:.3f}',  # Value to display
        ha='center',  # Horizontal alignment
        va='bottom'  # Vertical alignment
    )

# Add labels, title, and legend
ax.set_xlabel('Configurations')
ax.set_ylabel('Values')
ax.set_title('JMH Benchmark for Write Concern -- Single Node Replica Set')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')  # Rotate labels for better readability

# Optionally, add a grid
ax.yaxis.grid(True)

# Save the plot
plt.savefig('histogram/jmh_wc_single.png')


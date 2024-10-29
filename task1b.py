import time
from generate_random_graph import generate_random_graph
from dijkstra import dijkstra
import matplotlib.pyplot as plt
import numpy as np

sizes = list(range(100, 1100, 100))
execution_times = []

# Test algorithm with different network sizes
for num_of_vertices in sizes:
    # start timer
    start = time.time()

    # TODO: determine the path and journey duration in minutes between station pairs
    graph = generate_random_graph(num_of_vertices, 0.5, True, False, True, 0, 10)
    m, p = dijkstra(graph, 50)

    # completed algorithm, append the results
    execution_time = time.time() - start
    execution_times.append(execution_time)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot empirical data
plt.plot(sizes, execution_times, 'bo-', label='Empirical Time')

# Plot theoretical O(n^2) complexity
# Normalize theoretical curve to match empirical data scale
theoretical = np.array(sizes)**2
scaling_factor = np.mean(execution_times) / np.mean(theoretical)
theoretical = theoretical * scaling_factor
plt.plot(sizes, theoretical, 'r--', label='Theoretical O(n²)')

# Customize the plot
plt.xlabel('Network Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Dijkstra\'s Algorithm: Empirical vs Theoretical Time Complexity')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

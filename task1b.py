import time
from generate_random_graph import generate_random_graph
import matplotlib.pyplot as plt
import numpy as np
from task1b_utils import get_test_pairs, find_path

sizes = list(range(100, 1100, 100))
execution_times = []

# Test algorithm with different network sizes
for network_size in sizes:
    # start timer
    start = time.time()

    graph = generate_random_graph(network_size, 0.5, True, False, True, 0, 10)

    pairs = get_test_pairs(network_size, 30)

    for pair in pairs:
        path, total_distance = find_path(graph, pair[0], pair[1])

    # completed algorithm, append the results
    execution_time = time.time() - start
    execution_times.append(execution_time)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot empirical data
plt.plot(sizes, execution_times, label='Empirical Time')

# Calculate theoretical O(n²) values: size of network^2
theoretical = np.array(sizes)**2

# Calculate scaling factor to normalize the data
scaling_factor = np.mean(execution_times) / np.mean(theoretical)

# Apply normalization
theoretical = theoretical * scaling_factor

# Plot theoretical O(n^2) complexity
plt.plot(sizes, theoretical, label='Theoretical O(n²)')

# Add labels
plt.xlabel('Network Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Dijkstra\'s Algorithm: Empirical vs Theoretical Time Complexity')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

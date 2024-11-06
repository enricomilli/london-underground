import time
from generate_random_graph import generate_random_graph
import matplotlib.pyplot as plt
import numpy as np
from task1b_utils import get_test_pairs, find_path

sizes = list(range(100, 1100, 100))
execution_times = []

# Test algorithm with different network sizes
for network_size in sizes:

    graph = generate_random_graph(network_size, 0.3, True, False, True, 0, 10)

    pairs = get_test_pairs(network_size, 30)

    start = time.time()

    for pair in pairs:
        path, total_distance = find_path(graph, pair[0], pair[1])

    # execution time for all the pairs
    execution_time = time.time() - start

    # divide to get an avg execution time per pair
    avg_execution_time = execution_time / 30

    # append the avg exec time
    execution_times.append(avg_execution_time)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot empirical data
plt.plot(sizes, execution_times, label='Empirical Time')

theoretical = np.array(sizes)**2

# theoretical_exec_times = []
# for network_size in sizes:
#     # Expected number of edges with 0.5 probability
#     expected_edges = (network_size * (network_size - 1)) / 4

#     # Time complexity: O((E + V)log V)
#     theoretical_time = (expected_edges + network_size) * np.log(network_size)

#     theoretical_exec_times.append(theoretical_time)

scaling_factor = np.mean(execution_times) / np.mean(theoretical)

theoretical = theoretical * scaling_factor

plt.plot(sizes, theoretical, label='Theoretical O(n^2)')

# Add labels
plt.xlabel('Network Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Dijkstra\'s Algorithm: Empirical vs Theoretical Time Complexity')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

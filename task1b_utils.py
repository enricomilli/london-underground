import random
from dijkstra import dijkstra


def get_test_pairs(n_stations, n_pairs=30):
    test_pairs = []
    for _ in range(n_pairs):
        start = random.randint(0, n_stations-1)
        end = random.randint(start, n_stations-1)
        # Ensure we don't test same station and end is greater
        while end == start and end < start:
            end = random.randint(0, n_stations-1)

        test_pairs.append((start, end))
    return test_pairs



def find_path(G, start, end):
    # Run Dijkstra's algorithm from start station
    minutes, predecessors = dijkstra(G, start)

    # Reconstruct the path from end to start using predecessors
    path = []
    current = end

    # Check if end is reachable
    if predecessors[end] is None and start != end:
        return None, float('inf')  # No path exists

    # Work backwards from end to start
    while current is not None:
        path.append(current)
        current = predecessors[current]

    return path, minutes[end]

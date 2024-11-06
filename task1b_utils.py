import random
from dijkstra import dijkstra

def get_test_pairs(n_stations, n_pairs=30):
    test_pairs = []

    # for each pair
    for _ in range(n_pairs):
        start = random.randint(0, n_stations-1)
        end = random.randint(start, n_stations-1)

        # Ensure the start isnt the destination
        while end == start:
            end = random.randint(0, n_stations-1)

        test_pairs.append((start, end))

    return test_pairs


def find_path(G, start, end):
    # Run Dijkstra's algorithm from start station
    distances, predecessors = dijkstra(G, start)

    # Start from the end so we can work with predecessors
    path = []
    current = end

    # If ending point has a predecessor it means it's reachable
    # The starting point should not be the destination
    if predecessors[end] is None and start != end:
        return None, None  # No path exists

    # while there is an current node
    while current is not None:
        # append current node to path
        path.append(current)

        # look up the current nodes predecessor
        current = predecessors[current]

    return path, distances[end]

def find_path_to_end(distances, predecessors, end):
    path = []
    current = end

    # If ending point has a predecessor it means it's reachable
    # The starting point should not be the destination
    if predecessors[end] is None:
        return None, None  # No path exists

    # while there is an current node
    while current is not None:
        # append current node to path
        path.append(current)

        # look up the current nodes predecessor
        current = predecessors[current]

    return path, distances[end]

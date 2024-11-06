from dijkstra import dijkstra
from task1b_utils import find_path_to_end


def test_connection_between_all_stations(graph, all_stations):
    failed_cases = []

    for station in all_stations:
        # use dijkstras and create source node
        distances, predecessors = dijkstra(graph , all_stations.index(station))

        for to_station in all_stations:
            if station == to_station:
                continue

            # get the journey to destination node
            path, total_minutes = find_path_to_end(distances, predecessors, all_stations.index(to_station))
            if path is None or total_minutes is None:
                failed_cases.append((station, to_station))


    return len(failed_cases) < 1, failed_cases

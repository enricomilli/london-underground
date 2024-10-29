from adjacency_list_graph import AdjacencyListGraph
from task1b_utils import find_path
from constants import UNDERGROUND_DATA_FILE
from read_file import get_underground_data
from utils import format_underground_data, get_all_stations, get_all_connections
from mst import kruskal
from task4b_utils import create_path_string
import matplotlib.pyplot as plt

underground_data = get_underground_data(UNDERGROUND_DATA_FILE)

formated_data = format_underground_data(underground_data)

all_stations = get_all_stations(formated_data)
all_connections = get_all_connections(formated_data)

underground_graph = AdjacencyListGraph(len(all_stations), False, True)

for edge in all_connections:
    try:
        from_station_index = all_stations.index(edge[0])
        to_station_index = all_stations.index(edge[1])
        travel_time = edge[2]
        underground_graph.insert_edge(from_station_index, to_station_index, travel_time)
    except RuntimeError:
        # print('already added this edge:', edge)
        pass


# Kruskals algorithm
minimum_spanning_tree = kruskal(underground_graph)
longest_journey = {
    "minutes": 0,
    "path": []
}
journey_times = []

# calculate all the possible journeys from every station
for station in all_stations:
    for to_station in all_stations:
        if station == to_station:
            continue

        path, total_minutes = find_path(minimum_spanning_tree, all_stations.index(station), all_stations.index(to_station))
        if total_minutes > longest_journey["minutes"]:
            longest_journey = {
                "minutes": total_minutes,
                "path": path
            }
        journey_times.append(total_minutes)

print(f'the longest journey is {longest_journey["minutes"]} minutes long.')
print("here is the journey:", create_path_string(all_stations, longest_journey["path"]))

# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(journey_times, bins=30, edgecolor='black')
plt.title('Distribution of London Underground Journey Durations')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()

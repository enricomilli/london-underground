from adjacency_list_graph import AdjacencyListGraph
from constants import UNDERGROUND_DATA_FILE
from dijkstra import dijkstra
from read_file import get_underground_data
from task1b_utils import find_path_to_end
from task4b_utils import create_path_string
from utils import format_underground_data, get_all_stations, get_all_connections
import matplotlib.pyplot as plt

# Use pandas to import the excel file
underground_data = get_underground_data(UNDERGROUND_DATA_FILE)

# format the data into a usable data structure
formated_data = format_underground_data(underground_data)

# get a list of all stations
all_stations = get_all_stations(formated_data)

# get a list of all edges
all_connections = get_all_connections(formated_data)

# create a adjacency list graph
underground_graph = AdjacencyListGraph(len(all_stations), False, True)

# add the edges to the adjacency list graph
for edge in all_connections:
    try:
        from_station_index = all_stations.index(edge[0])
        to_station_index = all_stations.index(edge[1])
        # weight of 1 to represent 1 stop / 1 station
        weight = 1
        underground_graph.insert_edge(from_station_index, to_station_index, weight)
    except RuntimeError:
        # Catch any repeated edges and continue
        pass


longest_journey = {
    "stations": 0,
    "path": []
}
journey_times = []

# calculate all the possible journeys from every station
for station in all_stations:

    # use dijkstras and create source node
    distances, predecessors = dijkstra(underground_graph, all_stations.index(station))

    for to_station in all_stations:
        if station == to_station:
            continue

        # find the path to the destination node
        path, total_stops = find_path_to_end(distances, predecessors, all_stations.index(to_station))

        # finding the longest path
        if total_stops > longest_journey["stations"]:
            longest_journey = {
                "stations": total_stops,
                "path": path
            }
        journey_times.append(total_stops)

print(f'the longest journey is {longest_journey["stations"]} stops long.')
print("here is the journey:", create_path_string(all_stations, longest_journey["path"]))

# Create the histogram
plt.figure(figsize=(10, 6))
plt.hist(journey_times, bins=30, edgecolor='black')
plt.title('Distribution of London Underground Journey Durations In Stops')
plt.xlabel('Number Of Stops')
plt.ylabel('Frequency')
plt.grid(True, alpha=0.3)
plt.show()

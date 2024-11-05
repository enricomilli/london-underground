from adjacency_list_graph import AdjacencyListGraph
from constants import UNDERGROUND_DATA_FILE
from read_file import get_underground_data
from utils import format_underground_data, get_all_stations, get_all_connections
from mst import kruskal

# Use pandas to import the excel file
underground_data = get_underground_data(UNDERGROUND_DATA_FILE)

# format the data into a usable data structure
formated_data = format_underground_data(underground_data)

# get a list of all stations
all_stations = get_all_stations(formated_data)

# get a list of all the edges
all_connections = get_all_connections(formated_data)

# create a adjacency list graph
underground_graph = AdjacencyListGraph(len(all_stations), False, True)

# add the edges to the adjacency list graph
for edge in all_connections:
    try:
        from_station_index = all_stations.index(edge[0])
        to_station_index = all_stations.index(edge[1])
        travel_time = edge[2]
        underground_graph.insert_edge(from_station_index, to_station_index, travel_time)
    except RuntimeError:
        # Catch any repeated edges and continue
        pass


# Kruskals algorithm to create the reduced service
minimum_spanning_tree = kruskal(underground_graph)
edge_list = minimum_spanning_tree.get_edge_list()

# Report the affected stops
for edge in edge_list:
    print(all_stations[edge[0]], "--", all_stations[edge[1]], end=", ")

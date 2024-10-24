from adjacency_list_graph import AdjacencyListGraph
from constants import UNDERGROUND_DATA_FILE
from read_file import get_underground_data
from utils import format_underground_data, get_all_stations, get_all_connections

underground_data = get_underground_data(UNDERGROUND_DATA_FILE)

formated_data = format_underground_data(underground_data)

all_stations = get_all_stations(formated_data)
all_connections = get_all_connections(formated_data)

underground_graph = AdjacencyListGraph(len(all_stations), True, True)

for edge in all_connections:
    try:
        from_station_index = all_stations.index(edge[0])
        to_station_index = all_stations.index(edge[1])
        travel_time = edge[2]
        underground_graph.insert_edge(from_station_index, to_station_index, travel_time)
    except RuntimeError:
        print('already added this edge:', edge)
        pass

print('program finished')

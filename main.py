from adjacency_list_graph import AdjacencyListGraph
from reading_file import read_excel_with_byte_reader, get_row_type
from constants import UNDERGROUND_DATA_FILE
from utils import get_all_stations, get_all_connections, format_underground_data

# Note: had to change the format of excel file to csv
# as there is no way to read a xlsx without a library
underground_data = read_excel_with_byte_reader(UNDERGROUND_DATA_FILE)

lines_data = format_underground_data(underground_data)

all_stations = get_all_stations(lines_data)
all_connections = get_all_connections(lines_data)

underground_graph = AdjacencyListGraph(len(all_stations), True, True)

for edge in all_connections:
    try:
        from_station_index = all_stations.index(edge[0])
        to_station_index = all_stations.index(edge[1])
        travel_time = edge[2]
        underground_graph.insert_edge(from_station_index, to_station_index, travel_time)
    except:
        print('already added this edge:', edge)
        pass

print('program finished')

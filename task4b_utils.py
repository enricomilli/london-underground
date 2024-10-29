
def create_path_string(all_stations, list_of_station_indexes):
    response = ""
    for station_index in list_of_station_indexes:
        response += " => " + all_stations[station_index]

    return response[4:]

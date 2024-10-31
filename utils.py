from constants import STATION_LIST_ENTRY, STATION_TRAVEL_TIME_ENTRY

def get_row_type(row):
    to_station = row[2]

    if type(to_station) is str:
        return STATION_TRAVEL_TIME_ENTRY
    if type(to_station) is float:
        return STATION_LIST_ENTRY
    else:
        print("this row was not read correctly:", row)
        return NotImplemented


def get_all_stations(lines_data):
    total = set()

    for line_name, line_info in lines_data.items():
        stations = line_info["stations"]
        for station in stations:
            total.add(station)

    return list(total)

def get_all_connections(lines_data):

    list_of_connections = []

    for line_name, line_info in lines_data.items():

        connections = line_info["connections"]

        list_of_connections.extend(connections)


    return list_of_connections


def format_underground_data(underground_data):
    lines_data = {}

    for row in underground_data:
        row_type = get_row_type(row)

        if row_type == STATION_LIST_ENTRY:
            station_name = row[1].strip()
            line_name = row[0].strip()


            if lines_data.get(line_name):
                lines_data[line_name]["stations"].append(station_name)
            else:
                lines_data[line_name] = {"stations": [station_name], "connections": []}

        elif row_type == STATION_TRAVEL_TIME_ENTRY:
            line_name = row[0].strip()
            from_station = row[1].strip()
            to_station = row[2].strip()
            travel_time = row[3]

            lines_data[line_name]["connections"].append(
                (from_station, to_station, int(travel_time))
            )

    return lines_data

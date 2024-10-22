from buffered_byte_array import BufferedByteReader
from constants import STATION_LIST_ENTRY, STATION_TRAVEL_TIME_ENTRY

def read_excel_with_byte_reader(filename):
    reader = BufferedByteReader(filename)
    data = []
    current_row = []
    current_cell = ""

    try:
        while True:
            # create byte from bits
            byte = 0
            for _ in range(8):
                # shift bits left to create space for new bit
                byte = (byte << 1) | reader.read_bit()

            # byte == 0 is the cell separator
            if byte == 0:
                if current_cell:
                    current_row.append(current_cell)
                    current_cell = ""

            # byte == 10 is the row separator
            elif byte == 10:
                if current_cell:
                # append to current cell before marking this row as complete
                    current_row.append(current_cell)

                if current_row:
                # append new row to the data as a list
                    data.append(current_row[0].split(","))

                # reset vars
                current_cell = ""
                current_row = []

            # a cell is being created
            else:
                # clean up unnecessary characters
                new_char = chr(byte)
                if new_char not in ["¿", "»", "ï", "\r"]:
                    current_cell += new_char

    except:
        pass

    # append the last row
    if current_cell:
        current_row.append(current_cell)
    if current_row:
        data.append(current_row[0].split(","))


    reader.close()
    return data


def get_row_type(row):
    str_num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "14", "16"]
    travel_time = row[3]
    to_station = row[2]

    if travel_time:
        return STATION_TRAVEL_TIME_ENTRY
    if not to_station:
        return STATION_LIST_ENTRY
    else:
        print("this row was not read correctly:", row)
        return NotImplemented

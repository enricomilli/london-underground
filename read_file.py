import pandas as pd

def get_underground_data(filename):
    excel = pd.read_excel(filename, header=None)

    return excel.values.tolist()

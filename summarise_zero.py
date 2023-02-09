# apps to perform summarisation of data files

import pandas as pd


def describe_file(file_path):
    try:
        # run if file exists
        d0 = pd.read_csv(file_path)
    except FileNotFoundError:
        msg = "Sorry, the file " + file_path + " does not exist."
        print(msg)
    else:
        # write the summary/ description file with _description appended to file name
        path_to_write_to = file_path.split('.csv')[0] + '_description.csv'
        d0.describe().to_csv(path_to_write_to)
        msg = "Summary desicription written to: " + path_to_write_to
        print(msg)
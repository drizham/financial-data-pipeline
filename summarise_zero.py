# apps to perform summarisation of data files

import pandas as pd
from utils_zero import create_directory


def describe_file(input,output):
    """Reads a csv (input) and runs a simple pandas describe on it
    saves the data to (output) """
    try:
        # run if input file exists
        d0 = pd.read_csv(input)
    except FileNotFoundError:
        msg = "Sorry, the file " + input + " does not exist."
        print(msg)
    else:
        # write the summary/ description file with _description appended to file name
        name_to_write_to = input.split('/')[-1]
        create_directory(output) # creates directory if it does not exist
        # TODO - add a try except to catch exeptions from pandas describe
        d0.describe().to_csv(output + name_to_write_to)
        msg = f'Summary written to {output + name_to_write_to}'
        print(msg)
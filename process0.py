from utils_zero import create_directory # util to create directories
import kensu.pandas as pd

def process_2_interim0(input, output):
    """processes *.csv files from 'raw' to 'interim0' standard
    Uses Kensu pandas *.csv write ensuring that the observability stats
    are sent to Kensu
    input - input file path
    output - output file path"""
    try:
        # run if input file exists
        d0 = pd.read_csv(input)
    except FileNotFoundError:
        msg = "Sorry, the file " + input + " does not exist."
        print(msg)
    else:
        # write the file ...
        name_to_write_to = input.split('/')[-1]
        create_directory(output) # creates directory if it does not exist
        full_path = f'{output}{name_to_write_to}'
        #d0.to_csv(output + name_to_write_to, index=False)
        d0.to_csv(full_path, index=False)
        msg = f'Processed to interim0 at: {full_path}'
        print(msg)
    return full_path
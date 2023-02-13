import csv
import os

def read_start_end_dates(file_path):
    
    # Open the file in 'r' mode, not 'rb'
    csv_file = open(file_path,'r')
    start = []
    end = []

    # Read off and discard first line, to skip headers
    csv_file.readline()

    # Split columns while reading
    for a, b in csv.reader(csv_file, delimiter=','):
        # Append each variable to a separate list
        start.append(a)
        end.append(b)
    return start, end

def create_directory(path):
    """creates a directory if it does not already exist"""
    try:
        if not os.path.exists(path):
            print(f'{path} does not exist')
            os.makedirs(path) # create path if needed
            print(f'{path} directory created')
            return
    except OSError:
        sys.exit('Fatal: output directory "' + path + '" does not exist and cannot be created')
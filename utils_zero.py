import csv

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
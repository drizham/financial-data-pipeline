# apps to perform summarisation of data files with observability

# small data preparation example to demonstrate the results of using kensu-py
#import kensu.pandas as pd # import pandas as pd
import kensu.pandas as pd # import pandas as pd
from utils_zero import create_directory
from init_observability import init_kensu

# for sending custom data to Kensu
import kensu.exp
from kensu.exp import create_publish_for_data_source

def describe_file(input,output):
    """Reads a csv (input) and runs a simple pandas describe on it
    saves the data to (output) """
    try:
        init_kensu('summariser') # this works
    except TypeError:   
        msg = "Unable to initialize kensu, ensure tokens and ingestion url are correct"
        print(msg)
    else:
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
            d0.describe().to_csv(output + name_to_write_to, index=False)
            msg = f'Summary desciption written to {output + name_to_write_to}'
            print(msg)

            try:
                # send lineage data to kensu
                source0 = input # data source
                sink0 = output + name_to_write_to # data sink
                create_publish_for_data_source(name=source0, format='csv', location = source0, schema=None)
                create_publish_for_data_source(name=sink0, format = 'csv' , location = sink0, schema=None)
                kensu.exp.link(input_names=[source0], output_name=sink0)         
            except Exception as e:
                print(e)
                print('Unable to add lineage data for summariser')
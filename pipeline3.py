import manage_lake
import download_zero as dz
import calendar_utils
import direction_suggester0
import glob
import process0 as proc0
import table_builder
from init_observability import init_kensu

def main(ticker, year, lake):
    print(f'Downloading {ticker}, data for {year} to {lake}')

    # remove all previously downloaded / processed data from folder
    manage_lake.delete_files(f'{lake}{ticker}/raw/')
    manage_lake.delete_files(f'{lake}{ticker}/description/')
    manage_lake.delete_files(f'{lake}{ticker}/interim0/')
    # get list of start and end dates to download data
    # & save to a separate *.csv file
    week_start_dates = calendar_utils.week_start_dates(year)
    week_end_dates = calendar_utils.week_end_dates(year)

    # download ticker data for the year
    # save each weeks' data as a *.csv file
    dz.download_instrument_2_csv0(ticker, week_start_dates, week_end_dates, lake)

    # call a 'processor' that processes each data *.csv file
    # & collects and transmit observability stats from each file
    print('Processing raw data files to interim0')
    try:
        init_kensu('interim0 file processor') # sets the name of application in Kensu
    except TypeError:   
        msg = "Unable to initialize kensu, ensure tokens and ingestion url are correct"
        print(msg)
    else:
        flist = glob.glob(f'{lake}{ticker}/raw/*.csv') # get the list of downloaded files
        for file in sorted(flist):
            proc0.process_2_interim0(file, f'{lake}{ticker}/interim0/')

    print('Processing interim0 data files to build table 0 - bronze class table')
    try:
        init_kensu('table 0 builder') # sets the name of application in Kensu
    except TypeError:   
        msg = "Unable to initialize kensu, ensure tokens and ingestion url are correct"
        print(msg)
    else:
        table_builder.build0(lake, ticker)




"""     # check data quality for each file before using data
    expected_types = ['O', 'float64', 'float64', 'float64',
       'float64', 'int64', 'float64', 'float64']
    
    # runs through all the *.csv files and outputs the recomended direction
    # of trade for the next week
    # .market_direction1 calls the basic quality checks directly
    direction_suggester0.market_direction1(lake, ticker, expected_types) """

main('CL=F', 2022, 'lake1/')
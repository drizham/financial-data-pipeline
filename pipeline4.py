import manage_lake
import download_zero as dz
import glob
import process0 as proc0
import table_builder
from init_observability import init_kensu
import utils_zero as uz

def pipeline4(ticker, start_date, end_date, lake):
    print(f'Downloading {ticker}, data from {start_date} - {end_date} to {lake}')
    # download ticker data for timeframe and save as a *.csv file
    raw_path = dz.yf_2_csv1(ticker, start_date, end_date, lake)
    print(f'data downloaded and saved to {raw_path}')

    # call a 'processor' that processes each data *.csv file
    # & collects and transmit observability stats from each file
    print('Processing raw data files to interim0')
    
    init_kensu('interim0 file processor') # sets the name of application in Kensu
    interim_path0 = proc0.process_2_interim0(raw_path, f'{lake}{ticker}/interim0/')
    print(f'data processed to interim0 at: {interim_path0}')

    print('Processing interim0 data files to build table 0 - bronze class table')
    
    init_kensu('table 0 builder') # sets the name of application in Kensu
    print(f'interim_path0: {interim_path0}')
    table_builder.build0(lake, ticker, interim_path0, 'table0_bronze.csv')


def call_pipeline(ticker, start_date, end_date, lake):
    # call pipeline 4
    # call with ticker, start date, end date, lake
    # example start and end dates
    """ 
    ticker - 'CL=F'
    start_date - 2023-01-02,2023-01-07
    end_date - 2023-01-09,2023-01-14
    lake - 'lake1/'
    """
    pipeline4(ticker, start_date, end_date, lake)


# get start and end dates from file for range to download data
start_dates, end_dates = uz.read_start_end_dates('start_end_dates.csv')

def main(ticker, lake, date_file):
    # read start and end dates for data downloads
    start_dates, end_dates = uz.read_start_end_dates(date_file)
    # remove all previously downloaded / processed data from folders
    manage_lake.delete_files(f'{lake}{ticker}/raw/')
    #manage_lake.delete_files(f'{lake}{ticker}/description/')
    manage_lake.delete_files(f'{lake}{ticker}/interim0/')
    for x in range(len(start_dates)):
        pipeline4(ticker, start_dates[x], end_dates[x], lake)

main('CL=F', 'lake1/', 'start_end_dates.csv')
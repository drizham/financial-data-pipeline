# over arching financial data downloader
import yfinance as yf
from utils_zero import create_directory # util to create directories
import os
# for sending custom data to Kensu
import kensu.exp
from kensu.exp import create_publish_for_data_source
from init_observability import init_kensu


def download_instrument_2_csv0(symbol,week_start_dates, week_end_dates,
                                folder):
    """wrapper of yfinance data
    downloads and saves a few weeks of data as a single csv file in the folder"""
    #week_start_dates = ['2023-01-02', '2023-01-09', '2023-01-16', '2023-01-23', '2023-01-30']
    #week_end_dates = ['2023-01-07', '2023-01-14', '2023-01-21', '2023-01-28', '2023-02-04']
    # yfinance intervals => 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    # folder is the folder path to download to

    try:
        init_kensu('yf downloader') # sets the name of application in Kensu
    except TypeError:   
        msg = "Unable to initialize kensu, ensure tokens and ingestion url are correct"
        print(msg)
    else:

        week_count = 1
        for x in range(len(week_start_dates)):
            try:
                print('Trying to download data for: ' + symbol)
                obj0 = yf.Ticker(symbol)
                #print('downloading data for week ' + str(week_count) + ' starting ' + week_start_dates[x] + ' ending ' + week_end_dates[x] )
                d0 = obj0.history(interval='1h', start=week_start_dates[x], end=week_end_dates[x])
                if d0.empty:
                    # print('No data downloaded for symbol:' + symbol)
                    raise Exception('Symbol is either invalid or delisted')
            except Exception as e:
                    print('No data downloaded for symbol: ' + symbol)
                    print(e)
                    break
            else:
                    print('Successfully downloaded data for: ' + symbol)
                    folder_path = folder + symbol + '/' + 'raw/' # + 'week' + str(week_count) + '.csv'
                    create_directory(folder_path) # creates directory if it does not exist
                    full_path = folder_path + 'we_' + week_end_dates[x] + '.csv'
                    # complete_path ensures that application lineage can be created from 
                    # an app using this function to the down stream apps.
                    complete_path = 'file:' + os.path.abspath(os.getcwd()) + '/' + full_path
                    d0.to_csv(full_path)
                    print('Downloaded data saved as: ' + full_path)
                    week_count = week_count + 1

            try:
                # send lineage data to kensu
                source0 = 'yahoo finance data provider' # free text field for data source
                # data source & sink for this data downloader
                create_publish_for_data_source(name=source0, format='API call', location = 'from yahoo finance API', schema=None)
                #create_publish_for_data_source(name=full_path, format = 'csv' , location = full_path, schema=None)
                create_publish_for_data_source(name=full_path, format = 'csv' , location = complete_path, schema=None)
                # links source and sink above for lineage in Kensu
                kensu.exp.link(input_names=[source0], output_name=full_path)         
            except Exception as e:
                print('Unable to add lineage data for source: yf download')
                print(e)
                break     
    return

# TODO - add different source of downloading data e.g. openbb

def yf_2_csv1(symbol,start_date, end_date,
                                folder):
    """wrapper of yfinance data
    downloads and saves data as a single csv file in the folder"""
    #week_start_date = '2023-01-02'
    #week_end_dates = '2023-01-07'
    # yfinance intervals => 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    # folder is the folder path to download to

    try:
        init_kensu('yf downloader') # sets the name of application in Kensu
    except TypeError:   
        msg = "Unable to initialize kensu, ensure tokens and ingestion url are correct"
        print(msg)
    else:
    #for x in range(len(week_start_dates)):
        try:
            print('Trying to download data for: ' + symbol)
            obj0 = yf.Ticker(symbol)
            d0 = obj0.history(interval='1h', start=start_date, end=end_date)
            if d0.empty:
                # print('No data downloaded for symbol:' + symbol)
                raise Exception('Symbol is either invalid or delisted')
        except Exception as e:
                print('No data downloaded for symbol: ' + symbol)
                print(e)
        else:
                print('Successfully downloaded data for: ' + symbol)
                folder_path = folder + symbol + '/' + 'raw/' # + 'week' + str(week_count) + '.csv'
                create_directory(folder_path) # creates directory if it does not exist
                full_path = folder_path + 'we_' + end_date + '.csv'
                # complete_path ensures that application lineage can be created from 
                 # an app using this function to the down stream apps.
                complete_path = 'file:' + os.path.abspath(os.getcwd()) + '/' + full_path
                d0.to_csv(full_path)
                print('Downloaded data saved as: ' + full_path)
        try:
            # send lineage data to kensu
            source0 = 'yahoo finance data provider' # free text field for data source
            # data source & sink for this data downloader
            create_publish_for_data_source(name=source0, format='API call', location = 'from yahoo finance API', schema=None)
            #create_publish_for_data_source(name=full_path, format = 'csv' , location = full_path, schema=None)
            create_publish_for_data_source(name=full_path, format = 'csv' , location = complete_path, schema=None)
            # links source and sink above for lineage in Kensu
            kensu.exp.link(input_names=[source0], output_name=full_path)         
        except Exception as e:
            print('Unable to add lineage data for source: yf download')
            print(e)    
    return
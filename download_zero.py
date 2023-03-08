# over arching financial data downloader
import yfinance as yf
from utils_zero import create_directory # util to create directories
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
                d0 = obj0.history(interval='1d', start=week_start_dates[x], end=week_end_dates[x])
                if d0.empty:
                    # print('No data downloaded for symbol:' + symbol)
                    raise Exception('Symbol is either invalid or delisted')
            except Exception:
                    print('No data downloaded for symbol: ' + symbol)
                    break
            else:
                    print('Successfully downloaded data for: ' + symbol)
                    folder_path = folder + symbol + '/' + 'raw/' # + 'week' + str(week_count) + '.csv'
                    create_directory(folder_path) # creates directory if it does not exist
                    full_path = folder_path + 'week' + str(week_count) + '.csv'
                    d0.to_csv(full_path)
                    print('Downloaded data saved as: ' + full_path)
                    week_count = week_count + 1

            try:
                # send lineage data to kensu
                source0 = 'yahoo finance data provider' # free text field for data source
                # data source & sink for this data downloader
                create_publish_for_data_source(name=source0, format='API call', location = 'from yahoo finance API', schema=None)
                create_publish_for_data_source(name=full_path, format = 'csv' , location = full_path, schema=None)
                # links source and sink above for lineage in Kensu
                kensu.exp.link(input_names=[source0], output_name=full_path)         
            except Exception as e:
                print('Unable to add lineage data for source: yf download')
                print(e)
                break     
    return

# TODO - add different source of downloading data e.g. openbb
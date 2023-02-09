# over arching downloader
import yfinance as yf

def download_instrument_2_csv0(symbol,week_start_dates, week_end_dates):
    """wrapper of yfinance data
    downloads and saves a few weeks of data as a single csv file in the folder"""
    # default start and end dates
    # TODO - abstract out if needed in the future
    #week_start_dates = ['2023-01-02', '2023-01-09', '2023-01-16', '2023-01-23', '2023-01-30']
    #week_end_dates = ['2023-01-07', '2023-01-14', '2023-01-21', '2023-01-28', '2023-02-04']
    
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
                path_string = 'data/week' + str(week_count) + '.csv'
                d0.to_csv(path_string)
                print('Downloaded data saved as: ' + path_string)
                week_count = week_count + 1
    return
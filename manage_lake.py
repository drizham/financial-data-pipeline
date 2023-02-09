# all the utilities to manage the 'data lake'
import glob
import os

def remove_downloaded_csv():
    # get list of data files previously downloaded
    flist = glob.glob("data/week*.csv")
    number_of_files = len(flist)
    if (number_of_files):
        print(str(number_of_files) + ' downloaded instrument data files found')
        print('Deleting previous downloads')
        # delete previously downloaded files 
        for f in flist:
            fname = f.rstrip()
            if os.path.isfile(fname):
                os.remove(fname)
    else:
        print('No downloaded instrument data files found')
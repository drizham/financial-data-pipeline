# all the utilities to manage the 'data lake'
import glob
import os

def delete_files(path):
    """Deletes files in a folder"""
    # include / in path e.g. path = 'data/lake/folder_to_clear/'
    flist = glob.glob(f'{path}week*.csv')
    number_of_files = len(flist)
    if (number_of_files):
        print(str(number_of_files) + ' data files found')
        print(f'Deleting files from {path}')
        # delete files 
        for f in flist:
            fname = f.rstrip()
            if os.path.isfile(fname):
                os.remove(fname)
    else:
        print('No data files found')
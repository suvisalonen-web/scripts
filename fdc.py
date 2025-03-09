#
# fdc - files directory count
#

import os
import time


def fdirCount(path):

    files, dirs= 0, 0
    for root, dirnames, filenames in os.walk(path):
        dirs+= len(dirnames)
        files += len(filenames)

    # return the variables dirs and files as a tuple
    return (files, dirs)     

print('Type your directory')

path=input()

start=time.time()
files,dirs=fdirCount(path)
end=time.time()
elapsed=end-start


# Grand Total
print('Files:', files)
print('Directories:', dirs)
print('Elapsed time:',elapsed, '(sec)')




    

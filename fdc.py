#
# fdc - files directory count
#

import os
import time

print('Type your directory')

path=input()
start=time.time()

files, dirs= 0, 0
for root, dirnames, filenames in os.walk(path):
    dirs+= len(dirnames)
    files += len(filenames)

end=time.time()
elapsed=end-start

# Grand Total
print('Files:', files)
print('Directories:', dirs)
print('Elapsed time (sec)',elapsed)




    

import shutil
import os
import time

#set where the source of the files are
source = '/Users/harri/Onedrive/Desktop/Folder C/'


#set the destination path to folder D
destination = '/Users/harri/Onedrive/Desktop/Folder D/'
files = os.listdir(source)

for i in files:
    #we are saying move the files represented by 'i' to their new destination

    f = open(r'/User/harri/Onedrive/Desktop/Folder F/', 'r')

    while True:

        line = f.readline()
        if not line:
            time.sleep(1)
            print ('No changes have been made')
        else:
            print('Incorrect')
        

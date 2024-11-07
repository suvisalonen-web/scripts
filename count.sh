#!/bin/sh


# step 1
#echo "current directory"
#pwd

#step 2
echo "Changing to /bin"
cd /bin
echo "Number of files: `ls -lrt | wc -l`"

#step 3
echo "Changing to /var"
cd /var
echo "Number of files: `ls -lrt | wc -l`"


echo "Author: Suvi"
echo "Version: 1.1"

#!/bin/sh


# step 1
echo "current directory"
pwd

#step 2
echo "changing to /bin"
cd /bin
echo "number of files: `ls -lrt | wc -l`"

#step 3
echo "changing to /var"
cd /var
echo "number of files: `ls -lrt | wc -l`"


echo "Author: Suvi"
echo "Version: 1.0"

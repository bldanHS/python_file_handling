import os
from os import path
from os import mkdir
from os import listdir

numofbytes = 0
numof_dirs = 0

source = path.realpath("./")

directory = "results"

mkdir(directory)

dirs = listdir(source)

f = open("results/results.txt", "w+")
for i in dirs:
    if os.path.isfile(i):
        numofbytes += os.stat(i).st_size
        f.write(i+ "\n")
f.write("The number of bytes of files in this directory is" + str(numofbytes))
f.close()



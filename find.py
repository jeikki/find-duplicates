import time
from time import gmtime, strftime
import datetime
import os
import hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

#dirpath = 'c:\\projects\\hc2\\'
#dirpath = 'c:\\Users\\oinasj.EMEA\\OneDrive\\Pictures\\2019\\NZ\\Other'
dirpath = 'c:\\Users\\oinasj.EMEA\\OneDrive\\Pictures\\'
print("current directory is : " + dirpath)

outputfile = "duplicates.csv"
outputfilepath = os.getcwd() + "\\" + outputfile

exists = os.path.isfile(outputfile)
if exists:
    print(outputfile + "_" + strftime("%Y%m%d%H%M%S", gmtime()))
    os.rename(outputfile, (outputfile + "." + strftime("%Y%m%d%H%M%S", gmtime())))
    print("file " + outputfile + " exists. Removing...")

opfile = open(outputfile, "a")
print("Output file " + outputfile + " created.")

md5s = []
sizes = []
files = []

id = 0
# r=root, d=directories, f = files
for r, d, f in os.walk(dirpath):
    for file in f:
        filepath = os.path.join(r, file)
        #md5s.append(md5(filepath))
        sizes.append(os.path.getsize(filepath))
        files.append(filepath)

filecount = len(files)
#exptime_s = filecount * 5
exptime_s = filecount * 0.04
exptime_min = exptime_s / 60

print("File count: ", filecount)
#print("Expected time: ", exptime_min, " minutes")
print("Expected time: ", exptime_s, " seconds")

totalsize = 0

start1 = time.time_ns()
for f in files:
    start = time.time_ns()
    for f2 in files:
        if f != f2:
            if os.path.getsize(f) == os.path.getsize(f2):
                #if md5(f) == md5(f2):
                    #opfile.write(f + "," + f2)
                print(f + "," + f2)
                print(os.path.getsize(f), ",", os.path.getsize(f2))
                totalsize += os.path.getsize(f)
                #print(md5(f) + " == " + md5(f2))
    end = time.time_ns() - start
    end /= 1000
    end /= 1000
    end /= 1000
    print(end)
end = time.time_ns() - start1
end /= 1000
end /= 1000
end /= 1000
print(end)

print("Total size of duplicated files: \n", totalsize, "B\n", (totalsize/1000), "kB\n", (totalsize/1000/1000), "MB\n", (totalsize/1000/1000/1000), "GB\n")





import os

sfilename = r"e:\classroom\python\dec10\names.txt"
tfilename = "temp.txt"

sf = open(sfilename,"rt")
tf = open(tfilename,"wt")

for line in sf.readlines():
    if len(line) > 1:  # do we have more than just \n
        tf.write(line)

sf.close()
tf.close()

# delete source file
os.remove(sfilename)

# rename target as source
os.rename(tfilename,sfilename)


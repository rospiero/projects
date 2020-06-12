#not a very useful app, but can be used to convert file and reconvert file.



# you should change the folder to the one where you have the file:
import os
os.chdir("C:\\cancella")

#I will the file in binary(rb,wb) and in read mode and write mode:

with open('file.jpg', "rb") as rf:
    with open('convert.txt', "wb") as wf:
        for line in rf:
            wf.write(line)

#to then recompose the file:

with open('convert.txt', "rb") as rf:
    with open('file.jpg', "wb") as wf:
        for line in rf:
            wf.write(line)

file = open("text.txt", "r")
print(file.read())
file.close()

#read using with

with open("text.txt", "r") as data:
    print(data.read())



#r: Open for reading (default)
#w: Open for writing, truncating the file first
#x: Open for exclusive creation, failing if the file already exists
#a: Open for writing, appending to the end of the file if it exists
#b: Open in binary mode
#t: Open in text mode (default)
#+: Open for updating (reading and writing)

#append data
with open("text.txt", "a+") as data:
    data.write("\nadded some shit here")

with open("text.txt", "r") as data:
    print(data.read())

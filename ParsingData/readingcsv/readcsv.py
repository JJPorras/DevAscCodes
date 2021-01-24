import csv

file = open("csvdoc.csv") # open the file
reader = csv.reader(file) # now use the csv library to reader

#some methods heres
data = list(reader)
print(str(data[0]) + "\n")

#also posible using with and you can iterate
with open("csvdoc.csv") as data:
    list = csv.reader(data)
    for row in list:
        print(row)

#yes you can write by creating a writer object

new = ["R7", "192.168.1.1", "Costa Rica"]

with open("csvdoc.csv", "a") as data:
    writer = csv.writer(data)
    writer.writerow(new)

with open("csvdoc.csv") as data:
    list = csv.reader(data)
    for row in list:
        print(row)

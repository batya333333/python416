import csv

with open('data2.csv') as f:
    file_read = csv.reader(f, delimiter=';')
    for row in file_read:
        print(row)

import csv

with open("journey.tsv") as f:
    reader = csv.reader(f,delimiter='\t')
    print(list(reader)[1:3])
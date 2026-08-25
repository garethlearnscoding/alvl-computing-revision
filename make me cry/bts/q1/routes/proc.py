import csv
import pickle
import pprint

with open("bus_routes.pkl","rb") as f:
    data = pickle.load(f)

to_write = []

for (serNo,direc),stops in data.items():
    lst = [i[1] for i in list(sorted([ [i["stop_no"],i["stop_code"]] for i in stops],key=lambda x:x[0]))]
    tmp = [serNo,direc,",".join(lst)]
    to_write.append(tmp)

to_write.sort(key=lambda x:(x[0],x[1]))

with open("routes.tsv","w",newline="") as f:
    writer = csv.writer(f,delimiter='\t')
    writer.writerows(to_write)
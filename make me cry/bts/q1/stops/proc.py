import pickle
import csv

with open("bus_stops.pkl","rb") as f:
    data = pickle.load(f)

stops_dict = {i[0]:i[1] for i in data}

with open("stops_dict.pkl","wb") as f:
    pickle.dump(stops_dict,f)

with open("stops.tsv","w",newline="") as f:
    writer = csv.writer(f,delimiter='\t')
    writer.writerows(data)







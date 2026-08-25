import pickle
import json

with open("bus_stop.json","rb") as f:
    data = json.load(f)

data = data["value"]

stops_dict = {i["BusStopCode"]:i["Description"] for i in data}

with open("stops_dict.pkl","wb") as f:
    pickle.dump(stops_dict,f)
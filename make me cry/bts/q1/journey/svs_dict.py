from collections import defaultdict
import pickle




with open("bus_routes.pkl","rb") as f:
    data = pickle.load(f)

print(*data.items(),sep="\n\n")

stop_svs = defaultdict(list)

for key,stops in data.items():
    for i in stops:
        stop_svs[i["stop_code"]] += [key]

print(*stop_svs.items(),sep='\n')

with open("svs.pkl","wb") as f:
    pickle.dump(stop_svs,f)
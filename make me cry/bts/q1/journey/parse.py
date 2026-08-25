import pickle


stops = [46399,46289]

with open("stops_dict.pkl","rb") as f:
    stops_dict = pickle.load(f)

for i in stops:
    print("{"+f"\"stop_code\":\"{i}\", \"stop_name\":\"{stops_dict[str(i)]}\""+"}")

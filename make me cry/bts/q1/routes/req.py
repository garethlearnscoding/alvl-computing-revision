from collections import defaultdict
from pathlib import Path
import requests
import os
from dotenv import load_dotenv
import pickle


env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)


load_dotenv()

counter = defaultdict(list)

API_URL = "https://datamall2.mytransport.sg/ltaodataservice/BusRoutes"
API_KEY = os.environ["ACCOUNT_KEY"]

headers = {
    "AccountKey": API_KEY
}

skip = 0
limit = 500

while True:
    params = {}

    if skip > 0:
        params["$skip"] = skip

    r = requests.get(
        API_URL,
        headers=headers,
        params=params
    )
    r.raise_for_status()

    data = r.json()

    # Process this batch
    data = data["value"]
    
    for stop in data:
        serNo = stop["ServiceNo"]
        direc = stop["Direction"]
        counter[(serNo,direc)] += [{
            "stop_no": stop["StopSequence"],
            "stop_code":stop["BusStopCode"]
        }]

    # Stop if this was the final batch
    if len(data) < limit:
        break

    skip += limit

data = dict(counter)

with open("bus_routes.pkl", "wb") as f:
    pickle.dump(data, f)

import requests
import os
from dotenv import load_dotenv
from pathlib import Path
import pickle


env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)


API_URL = "https://datamall2.mytransport.sg/ltaodataservice/BusStops"
API_KEY = os.environ["ACCOUNT_KEY"]

headers = {
    "AccountKey": API_KEY
}

skip = 0
limit = 500

stops = []

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
    
    data = [
        [
            i["BusStopCode"],
            i["Description"],
            i["RoadName"]
        ]
    
        for i in data
    ]

    stops += data

    # Stop if this was the final batch
    if len(data) < limit:
        break

    skip += limit

print(stops)

with open("bus_stops.pkl", "wb") as f:
    pickle.dump(stops, f)

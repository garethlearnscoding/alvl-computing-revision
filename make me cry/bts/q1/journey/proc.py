import pickle
import csv
import random
from datetime import date, datetime, time, timedelta

"""
0. Journey ID
1. Random bus stop
2. Random bus on the bus stop
3. Random end stop
4. Random confirm of transfer
5. Random bus chosen based on prev end stop
6. Random end stop
7. Random confirm of transfer

-> Max 3 transfer
"""

def random_date():
    start = date(2026, 10, 7)
    end = date(2026, 11, 27)
    days = (end-start).days
    d = random.randint(1,days)
    return start+timedelta(days=d)

def random_time():
    random_time = time(
        random.randint(0, 23),
        random.randint(0, 59)
    )
    return random_time

def random_dt():
    rand_date = random_date()
    rand_time = random_time()

    rand_dt = datetime.combine(rand_date,rand_time)
    return rand_dt

def random_travel(n,dt):
    delta = sum([random.randint(2,6) for _ in range(n)])
    elaspe = dt + timedelta(minutes=delta)
    return elaspe
    

with open("svs.pkl","rb") as f:
    # Bus services based on bus stop code | key: BusStopCode, value: buses
    svs = pickle.load(f)

with open("bus_routes.pkl","rb") as f:
    bs_rts = pickle.load(f)

with open("stops_dict.pkl","rb") as f:
    stops_dict = pickle.load(f)

def main():
    j = 1
    to_write = []
    for s in range(1,60):
        student_id = f"S{s:04d}"
        for _ in range(1,51):
            journey_id = f"J{j:04d}"
            # journey_stop = {"journey_id":journey_id,"journey":[]}
            transfers = random.randint(1,3)
            start_dt = random_dt()
            bus,stops = random.choice(list(bs_rts.items()))
            subtracted = len(stops)-1
            
            n = random.randint(0,subtracted)

            start_stop = stops[n]["stop_code"]

            for i in range(transfers):

                delta = random.randint(1,len(stops)-n)

                end_stop = stops[n+delta-1]["stop_code"]

                end_dt = random_travel(delta,start_dt)

                to_write.append([journey_id,student_id,start_dt.strftime("%Y-%m-%d %H:%M"),end_dt,bus[0],bus[1],start_stop,end_stop])


                bus = random.choice(svs[end_stop])
                stops = bs_rts[bus]
                start_stop = end_stop
                start_dt = end_dt
                for idx,val in enumerate(stops,start=1):
                    if val["stop_code"] == start_stop:
                        n = idx

                if len(stops)-n == 0:
                    break

            j += 1

    random.shuffle(to_write)        

    with open("journey.tsv","w",newline="") as f:
        writer = csv.writer(f,delimiter="\t")
        writer.writerows(to_write)

main()
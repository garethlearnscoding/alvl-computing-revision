import csv
from pprint import pprint

def read_file():
    with open("ratings.csv") as f:
        data = list(csv.reader(f))[1:]

    names = "ABCDEFGHI"

    ratings = {i:{} for i in names}

    for i in data:
            ratings[i[0]][i[1]] = i[-1]

    return ratings

pprint(read_file())

def cal_hap(grid,ratings):
    tot_hap = 0
    n = len(grid)
    for i in range(n):
        for j in range(n):
             pov = grid[i][j]
             tot += 
             
         
     


def copy(grid):
     return [[j for j in i] for i in grid]


## Condition: A has to always seat at the top left of the grid

def gen_seat(ratings):
    no = len(ratings.keys())
    grid = [["None"]*no for _ in range(no)]
    grid[0][0] = "A"

    def _helper(grid,ratings,tot_hap = 0,):
        
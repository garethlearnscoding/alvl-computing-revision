def spiral(n):

    char_lst = [i for i in range(1,n**2+1)]

    even = n%2 ==0

    times = 0

    char_lst.reverse()

    corr_dict = {
        "r":"l",
        "l":"r",
        "d":"u",
        "u":"d"
    }

    move_dict = {
        "r":(0,1),
        "l":(0,-1),
        "d":(1,0),
        "u":(-1,0)
    }
    if even:
        dir_1u ="l"
        dir_rep ="u"
        r,c = 1,0
        r_range,c_range = [0,1],[0,0]
    else:
        dir_1u ="r"
        dir_rep ="d"
        r,c= -1,0
        r_range,c_range=[-1,0],[0,0]


    matrix = [[char_lst.pop(0)],[char_lst.pop(0)]]

    count = 2
    internal_track = -1


    for idx in range(len(char_lst)):
        if internal_track == -1:
            to_add = move_dict[dir_1u]
            r,c = r+to_add[0],c+to_add[1]
            dir = dir_1u
        else:
            to_add = move_dict[dir_rep]
            r,c = r+to_add[0],c+to_add[1]
            dir = dir_rep
            
        r_ins = r-r_range[0]


        if r < r_range[0]:
            matrix.insert(0,[char_lst[idx]])
            r_range[0] -= 1

        elif r>r_range[1]:
            matrix.append([char_lst[idx]])
            r_range[1] += 1

        elif c<c_range[0]:
            matrix[r_ins].insert(0,char_lst[idx])
            c_range[0] -= 1

        
        elif c > c_range[1]:
            matrix[r_ins].append(char_lst[idx])
            c_range[1] += 1

        elif c_range[0] <= c <= c_range[1]:
            if dir in ["l","u"]:
                matrix[r_ins].insert(0,char_lst[idx])
            else:
                matrix[r_ins].append(char_lst[idx])

        

        

        internal_track += 1

        if internal_track == (count-1):
            internal_track = -1
            dir_1u,dir_rep = dir_rep,corr_dict[dir_1u]
            times += 1

            if times == 2:
                count += 1
                times = 0



        # print()



    return matrix



spirals = [spiral(i) for i in range(3,10)]

for i in spirals:
    print(*i,sep='\n')
    print()

for row in by5:
    print(list(zip(row[:-1],row[1:])))
    math = list(map(lambda x: x[0]-x[1], zip(row[:-1],row[1:])))
    print(math)

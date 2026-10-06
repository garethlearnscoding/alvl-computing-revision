def spiral(n):

    char_lst = [i for i in range(1,n**2+1)]

    even = n%2 ==0

    char_lst.reverse()

    move_dict = {
        "r":(0,1),
        "l":(0,-1),
        "d":(1,0),
        "u":(-1,0)
    }

    if even:
        dir ="l"
        r,c = 1,0
        r_range,c_range = [0,1],[0,0]
    else:
        dir ="r"
        r,c= -1,0
        r_range,c_range=[-1,0],[0,0]



    matrix = [[char_lst.pop(0)],[char_lst.pop(0)]]

    to_add = move_dict[dir]

    for idx in range(len(char_lst)):
        r,c = r+to_add[0],c+to_add[1]
            
        r_ins = r-r_range[0]


        if r < r_range[0]:
            matrix.insert(0,[n**2 - idx-2])
            r_range[0] -= 1
            dir = "r"
            to_add = (0,1)

        elif r>r_range[1]:
            matrix.append([n**2 - idx-2])
            r_range[1] += 1
            dir = "l"
            to_add = (0,-1)

        elif c<c_range[0]:
            matrix[r_ins].insert(0,n**2 - idx-2)
            c_range[0] -= 1
            dir = "u"
            to_add = (-1,0)
        
        elif c > c_range[1]:
            matrix[r_ins].append(n**2 - idx-2)
            c_range[1] += 1
            dir = "d"
            to_add = (1,0)

        elif c_range[0] <= c <= c_range[1]:
            if dir in ["l","u"]:
                matrix[r_ins].insert(0,n**2 - idx-2)
            else:
                matrix[r_ins].append(n**2 - idx-2)


        # print(*matrix,sep="\n")
        # print()

    return matrix



by5 = spiral(7)
print(*by5,sep='\n')


# spirals = [spiral(i) for i in range(26,29)]

# for i in spirals:
#     print(*i,sep='\n')
#     print()


def dataset(spiral):
    r_idxs,c_idxs,ele = [],[],[]
    for r_idx,r in enumerate(spiral):
        for c_idx,c in enumerate(r):
            r_idxs.append(r_idx)
            c_idxs.append(c_idx)
            ele.append(c)

    return c_idxs,r_idxs,ele

# import matplotlib.pyplot as plt
# from collections import Counter


# fig, axs = plt.subplots(len(spirals), 2, figsize=(6, 20))

# for idx,spiral in enumerate(spirals):
#     n = len(spiral[0])
#     y,x,index = dataset(spiral)


#     axs[idx,0].scatter(x,index)
#     axs[idx,0].set_title(f"N: {n} | Row")
     
#     axs[idx,1].scatter(y,index)
#     axs[idx,1].set_title(f"N: {n} | Column")


    

# # plt.tight_layout()
# plt.show()

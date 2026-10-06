def gen_char_lst(filename):
    with open(filename) as f:
        data = f.read().replace(" ","").strip().split(",")

    characters = [chr(int(d)) for d in data]
    return characters

# print(gen_char_lst("inputA.txt"))



def soln_2(char_lst):

    n = int(len(char_lst)**0.5)
    even = n%2 ==0

    matrix = [[None]*n for _ in range(n)]

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
        r,c = (n//2)-1,n//2
        curr_r,curr_c = r+1,c
        dir_1u ="l"
        dir_rep ="u"
    else:
        r,c = n//2,n//2
        curr_r,curr_c = r-1,c
        dir_1u ="r"
        dir_rep ="d"
    matrix[r][c] = char_lst.pop(0)

    matrix[curr_r][curr_c] = char_lst.pop(0)

    count = 2
    internal_track = -1

    print(*matrix,sep="\n")
    print("CUR",curr_r,curr_c)

    for idx in range(len(char_lst)):
        print("count",count)
        if internal_track == -1:
            print("dir 1u",dir_1u)
            to_add = move_dict[dir_1u]
            print("tup",to_add)
            curr_r,curr_c = curr_r+to_add[0],curr_c+to_add[1]
            print("add",curr_r,curr_c)
            print("track",internal_track)

        else:
            print("dir rep",dir_rep)
            to_add = move_dict[dir_rep]
            print("tup",to_add)
            curr_r,curr_c = curr_r+to_add[0],curr_c+to_add[1]
            print("add",curr_r,curr_c)
            print("track",internal_track)

        print(curr_r,curr_c)
        matrix[curr_r][curr_c] = char_lst[idx]

        internal_track += 1

        if internal_track == (count-1):
            internal_track = -1
            dir_1u,dir_rep = dir_rep,corr_dict[dir_1u]
            times += 1

            if times == 2:
                count += 1
                times = 0

        print(*matrix,sep="\n")

        print()

    return matrix


result = soln_2(gen_char_lst("example.txt"))

for row in result:
    for char in row:
        print(char,end="")
    print()







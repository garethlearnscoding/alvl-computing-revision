def gen_char_lst(filename):
    with open(filename) as f:
        data = f.read().replace(" ","").strip().split(",")

    characters = [chr(int(d)) for d in data]
    return characters

print(gen_char_lst("inputA.txt"))



def soln_1(char_lst):
    n = int(len(char_lst)**0.5)

    flip_dict = {
        "v":"h",
        "h":"v"
    }

    total_moves = n*2 -1
    v= 0
    h = 0
    type = "v"

    r_c_count = []
    f=0
    for i in range(n):
        if i%2 == 0:
            r_c_count.append(f)
        else:
            r_c_count.append((n-1)-f)
            f+=1
    
    matrix = [[None]*n for _ in range(n)]

    for i in range(total_moves):
        no_ele = n - h if type == "v" else n-v

        eles = char_lst[0:no_ele]
        char_lst = char_lst[no_ele:]        

        fixed_axis = r_c_count[v] if type == "v" else n-1-r_c_count[h]

        # print("fa",fixed_axis)

        coords = [(i,fixed_axis) if type =="v" else (fixed_axis,i) for i in range(n)]

        # print(coords)
        if type=="v":
            if v%2 != 0:
                coords = coords[::-1]
                # print("v odd")
            else:
                # print("v even")
                ...
            top = h//2
            bot = h-top
            # print(top,bot)
            del coords[:bot]
            coords = coords[::-1]
            del coords[:top]
            coords = coords[::-1]
            
        else:
            if h%2 != 0:
                coords = coords[::-1]
                # print("h odd")
            else:
                # print("h even")
                ...
            top = v//2
            bot = v-top
            # print(top,bot)
            del coords[:bot]
            coords = coords[::-1]
            del coords[:top]
            coords = coords[::-1]

        # print(eles,coords)

        for i in range(no_ele):
            r,c = coords[i]
            ele = eles[i]
            matrix[r][c] = ele

        # print()
        print(*matrix,sep="\n")
        # print()

        if type == "v":
            v += 1
        else:
            h+=1 
        type = flip_dict[type]

    return matrix


result = soln_1(gen_char_lst("example.txt"))
for row in result:
    for char in row:
        print(char,end="")
    print()








def gen_char_lst(filename):
    with open(filename) as f:
        data = f.read().replace(" ","").strip().split(",")

    characters = [chr(int(d)) for d in data]
    return characters

# print(gen_char_lst("inputA.txt"))



def soln_3(char_lst):

    n = int(len(char_lst)**0.5)
    even = n%2 ==0


    for 








result = soln_3(gen_char_lst("example.txt"))

for row in result:
    for char in row:
        print(char,end="")
    print()







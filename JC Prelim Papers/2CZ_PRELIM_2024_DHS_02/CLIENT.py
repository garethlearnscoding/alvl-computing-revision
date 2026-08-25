def decompress(compressed_list,byte_rep,bytes_pattern):
    pat_lst = [bytes_pattern[i] + bytes_pattern[i+1] for i in range(0,len(bytes_pattern)-1,2)][::-1]
    for i in range(len(compressed_list)):
        if compressed_list[i] == byte_rep:
            del compressed_list[i]
            for j in range(len(pat_lst)):
                compressed_list.insert(i,pat_lst[j])
            return compressed_list
	
	
#main program

#type your client code here

import socket

s = socket.socket()

s.connect(('127.0.0.1',9999))


import csv

class SpiralMatrix:
    def __init__(self,n):
        self.n = n

        self.matrix = None
        self.r,self.c = None,None

        self.spacer = len(str(n**2)) + 3
        self._spiral()
        self._calculate_center()
        
    def _calculate_center(self):
        n = self.n
        self.r,self.c = n//2 - ((n%2)==0), n//2

    def __str__(self):
        parsed = ""
        for r in self.matrix:
            for c in r:
                parsed += f"{c:<{self.spacer}}"
            parsed += '\n'
        return parsed

    def _spiral(self):
        n = self.n
        even = n%2 ==0

        if even:
            to_add = (0,-1)
            r,c = 1,0
            r_range,c_range = [0,1],[0,0]
            matrix = [[n**2],[n**2 - 1]]    
        else:
            to_add = (0,1)
            r,c= -1,0
            r_range,c_range=[-1,0],[0,0]
            matrix = [[n**2-1],[n**2]]    



        for idx in range(n**2-2):
            r,c = r+to_add[0],c+to_add[1]
                
            r_ins = r-r_range[0]

            if r < r_range[0]:
                matrix.insert(0,[n**2 - idx - 2])
                r_range[0] -= 1
                to_add = (0,1)

            elif r > r_range[1]:
                matrix.append([n**2 - idx - 2])
                r_range[1] += 1
                to_add = (0,-1)

            elif c < c_range[0]:
                matrix[r_ins].insert(0,n**2 - idx - 2)
                c_range[0] -= 1
                to_add = (-1,0)
            
            elif c > c_range[1]:
                matrix[r_ins].append(n**2 - idx - 2)
                c_range[1] += 1
                to_add = (1,0)

            elif c_range[0] <= c <= c_range[1]:
                if to_add in [(0,-1),(-1,0)]:
                    matrix[r_ins].insert(0,n**2 - idx - 2)
                else:
                    matrix[r_ins].append(n**2 - idx - 2)

        self.matrix = matrix

    
    def cal_vert(self,r,c):
        return (self.n-c-1 if c>self.c else c)*2 + (c>self.c)

    def _to_csv(self,filename):
        pts_r = []
        pts_c = []
        for r in range(self.n):
            for c in range(self.n):
                pts_r.append([self.matrix[r][c]-1,r])
                pts_c.append([self.matrix[r][c]-1,c])
        pts_r.sort(key=lambda x:x[0])
        pts_c.sort(key=lambda x:x[0])
        with open(f"{filename}_r.csv","w",newline='') as f:
            writer = csv.writer(f)
            writer.writerows(pts_r)
        with open(f"{filename}_c.csv","w",newline='') as f:
            writer = csv.writer(f)
            writer.writerows(pts_c)

by5 = SpiralMatrix(12)

print(by5)

by5._to_csv("by11")
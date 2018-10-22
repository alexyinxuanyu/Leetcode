"""
3
5
10
20
"""
import sys
a=int(input())
b=int(input())
c=int(input())
d=int(input())
for i in range(a,a+2):
    for j in range(b,b+2):
        for z in range(c,c+2):
            if i+j+z==d:
                #print(i,j,z,d)
                print("Yes")
                sys.exit()
print("No")
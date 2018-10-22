"""
N M X Y
x1 x2 … xN
y1 y2 … yM
"""
import sys
one=list(map(int,input().split()))
two=list(map(int,input().split()))
two.sort()
three=list(map(int,input().split()))
three.sort()
for i in range(one[2]+1,one[3]+1):
    if two[-1]<i and three[0]>= i:
        print("No War")
        sys.exit()
print("War")
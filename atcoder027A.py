x=list(map(int,input().split()))
y=list(map(int,input().split()))
y.sort()
i=0
"""
while x[1]>0 and i<x[0]:
    x[1]-=y[i]
    i+=1
"""
num=0
for i in y:
    if x[1]-i>=0:
        num+=1
    x[1]-=i
if x[1]>0:
    print(num-1)
else:
    print(num)

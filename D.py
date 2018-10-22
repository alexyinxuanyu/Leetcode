"""
10 8 5 2
3 7
"""
one=list(map(int,input().split()))
second=list(map(int,input().split()))

def can(one,two):
    w=one[1]
    start=0
    z = 0
    while z<=one[0]:
        if not two:
            if one[0]<=one[1]:
                return True
            else:
                return False
        for i in two:
            if w-(i-start)<=one[3]:
                w=one[2]
                start=i
            elif w-(i-start)<=0:
                return False
            elif i-start==0:
                return False
            z += (i - start)
    return True
test=[[],]
for i in range(0,len(second)-1):
    w=[second[i]]
    for j in range(i,len(second)):
        test.append(w.append(second[j]))
num=0
for t in test:
    if can(one,t):
        print(t)
        num+=1
print(num)






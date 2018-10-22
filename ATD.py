"""
N M
for i in range(one[0]):
    w=1
    for i in range(one[1]):
        z=i
"""

one=list(map(int,input().split()))
#print(one)
z=[0]
def multip(begin,goal,time):
    if time == 0:
        if begin == goal:
            z[0] += 1
            return
        else:
            return
    #if time==0:
    #    return
    #if begin > goal:
    #    return
    #else:
    for i in range(1,goal+1):
        if time==one[0]:
            multip(i,goal,time-1)
        else:
            if begin<=goal:
                multip(begin*i, goal, time - 1)
            else:
                return
    return
multip(0,one[1],one[0])
print(z[0])





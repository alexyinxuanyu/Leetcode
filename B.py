"""
5 2 6 7
2 3
3 4
"""
one=list(map(int,input().split()))
w=[]
for i in range(one[1]):
    temp1=list(map(int,input().split()))
    w.append(temp1)
temp=[]
num=0
for i in w:
    for j in range(i[0],i[1]+1):
        if j not in temp:
            temp.append(j)
            num+=1
print(num*one[2]+(one[0]-num)*one[3])


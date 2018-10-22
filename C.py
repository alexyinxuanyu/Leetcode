"""
3 2
0 3 4
"""
import plistlib
z=[]
one=list(map(int,input().split()))
second=list(map(int,input().split()))
z=[second]
num=0
for i in range(one[1]):
    for p in range(len(z)):
        for j in range(one[0]):
            w=z[p][0:j]+[int(z[p][j]/2)]+z[p][j+1:]
            if w not in z:
                num+=1
                z.append(w)
    if i==0:
        if 0 not in second or 1 not in second:
            z.remove(second)
    print(z)
print(len(z)%(10**(9)+7))
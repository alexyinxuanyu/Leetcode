"""
if len(w)!=len(o):
    print("No")
    sys.exit()
count=0
for i in range(len(w)):
    if w[i]!=o[i]:
        count+=1
if count%2==0:
    print("Yes")
else:
    print("No")
"""
import sys
from collections import Counter
one=list(input())
#print(one)
two=list(input())
z={}
result=[]
for num,i in enumerate(one):
    if i not in z:
        z[i]=[num]
    else:
        z[i].append(num)
p={}
for num,i in enumerate(two):
    if i not in p:
        p[i]=[num]
    else:
        p[i].append(num)

print(p)
print(z)

w=[]
for k,v in z.items():
    if len(v)>1:
        w.append(v)
o=[]
for k,v in p.items():
    if len(v)>1:
        o.append(v)
print(w)
print(o)
"""
for i in w:
    if i not in o:
        print("No")
        sys.exit()
for i in o:
    if i not in w:
        print("No")
        sys.exit()
print("Yes")"""
"""


for k,v in z.items():
    if len(v)>1:
        temp=0
        for k1, v1 in p.items():
            if p[k1]==z[k]:
                temp=1
"""


z=w
w.sort()
#o.sort()
print(w==z)
print("Yes") if w==o else print("No")


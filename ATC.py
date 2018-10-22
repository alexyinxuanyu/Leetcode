"""
chokudai
redcoder
"""
import sys
from collections import Counter
one=list(input())
print(one)
two=list(input())
if len(one)!=len(two):
    print("No")
    sys.exit()
three=Counter(one)
print(one)
four=Counter(two)
print(two)
if len(three)!=len(four):
    print("No")
    sys.exit()
print("Yes")
L1=len(one)
list2=list(set(one))
list2.sort(reverse=False)
L2=len(list2)
print('集合:'+str(one))
for m in range(L2):
    X=set() #设定一个空的集合，用来存放这个元素的所在的位置
    start=one.index(list2[m])
    for n in range(L1):
        stop=L1
        if list2[m] in tuple(one)[start:stop]:
            a=one.index(list2[m],start,stop)
            X.add(a)
            start=start+1
    print('元素：'+str(list2[m])+'，一共有'+str(len(X))+'个，在列表位置集合为：'+str(X))















"""
s=[]
result={}
for i in three:
    if three[i]!=1:
        result[i]=[]

"""

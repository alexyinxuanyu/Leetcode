"""l="9001 cd.tail.com"
print("L: ",l)
l=l.split(' ')
l[0]=int(l[0])
print("L: ",l[0])
print(type(l[0]))
l[1]=l[1].split('.')
print("L1: ",l[1])
x='Blue,red,green'
x=x.split(',')
#print(x.split(','))
print(x)
#print(l.split())
s="wo shi SSSSS"
s=s.upper()
print(s)
z="-1"
if z[0] in ["-","+"]:
    print("negative")
z=[1,2,3,4,1,2,3]
j=1
if j in z:
    print("J in Z")
maxmum=max(z)
minxum=min(z)
i=[1,2]
print(i[0:1])
j=[2,3,1,2]
#if i in j:
print(i in j)

list1=[1,2,3]
list2=[2,3,4]
for i in list1:
    if i not in list2:
        print(i)

for i in range(len(list1)):
    list1.remove(list1[i])
    print(list1)
    i+=1
list2.remove(list1[2])"""
w=10
s=bin(w)
print(s)
s=s[2:]
print(s)

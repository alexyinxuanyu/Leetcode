x=1
y=4
number = 0
binx = str(bin(x))
print(binx)
biny = str(bin(y))
print(biny)
lenthmin = min(len(biny), len(binx))
numberzero=0
for j in range(lenthmin - 2):
    if binx[len(binx) - 1 - j] != biny[len(biny) - 1 - j]:
        number += 1
print(j)
if(len(biny)>=len(binx)):
    for i in range(2, len(biny) - j):
        print(biny)
        if biny[i]=='0':
            numberzero+=1
elif(len(biny)<len(binx)):
    for i in range(2, len(binx) - j):

        print(binx)
        if binx[i]=='0':
            numberzero+=1
print(numberzero)
print(number)
print(max(len(binx) - lenthmin, len(biny) - lenthmin))




print (number + max(len(binx) - lenthmin, len(biny) - lenthmin)-numberzero)

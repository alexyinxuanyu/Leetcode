str1 = str(bin(32))
# print(bin(32))
print(str1)

num = 0
sentry = 0
dis = 0
for i in range(len(str1)):
    if sentry != 0 and str1[i] == '1':
        end = i
        if dis < end - start:
            dis = end - start
        start = end
    elif str1[i] == '1':
        start = i
        sentry = 1
print(dis)

c = 10
p = str(c)
print(p)
for i in p:
    print(i)

sum = 0
cycle = 30
temp = str(2)
for i in temp:
    print(i)
while sum != 1 and cycle > 0:
    sum=0
    for i in temp:
        sum += int(i) ** 2
    print("sum: ",sum)
    temp = str(sum)
    cycle -= 1
if sum == 1:
    print("yes")
else:
    print("no")

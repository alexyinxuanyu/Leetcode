x=1
y=4
number = 0
num = 0
while x != 0 or y != 0:


    xnode = x % 2
    ynode = y % 2
    if xnode != ynode:
        num+=1
    number+=1
    if x >= 2 ** (number - 1):
        x -= 2 ** (number - 1)
    else:
        x = 0
    if y >= 2 ** (number - 1):
        y -= 2 ** (number - 1)
    else:
        y = 0
print (num)
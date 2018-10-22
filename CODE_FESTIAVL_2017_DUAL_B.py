import sys
from collections import Counter
candnum=int(input())
candiff=list(map(int,input().split()))
pronum=int(input())
prodiff=list(map(int,input().split()))

candiff=Counter(candiff)
prodiff=Counter(prodiff)
if pronum>candnum:
    print("NO")
    sys.exit()
for k,v in prodiff.items():
    if k in candiff:
        if candiff[k]<v:
            print("NO")
            sys.exit()
    else:
        print("NO")
        sys.exit()
print("YES")






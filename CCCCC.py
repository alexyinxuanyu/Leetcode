from collections import Counter as C
#print(C(input()).values()!=C(input()).values())
#print('YNeos'[(C(input()).values())!=C(C(input()).values())::2])
#C(C(input()).values())
#print(C(C(input()).values()))
#print('YNeos'[C(input()).values()!=C(input()).values()::2])
print('YNeos'[C(C(input()).values())!=C(C(input()).values())::2])
"""
azzel
apple
acbc
badd
"""
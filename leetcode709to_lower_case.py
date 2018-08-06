

"""
:type str: str
:rtype: str
 """
str2="Hello"
z = ""
for i in str2:
    if ord(i) >= 65 and ord(i) <= 90:
        z += str(ord(i) + 32)
    else:
        z += i
print(z)


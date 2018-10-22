"""
3 10
? A B
>
? C B
>
? A C
<
! BAC
"""
dic={1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H",9:"I",10:"J",11:"K",12:"L"
    , 13: "M",14:"N",15:"O",16:"P",17:"Q",18:"R",19:"S",20:"T",21:"U",22:"V",23:"W"
    , 24: "X",25:"Y",26:"Z"}
x=list(map(int,input().split()))
result=[]
for i in range(x[0]):
    result.append(chr(97+i))
for i in range(0,len(x[0])-1):
    for j in range(i+1,len(x[0])):
        query="?"+dic[i]+dic[j]
        print(query)
        w=input()
        if w==">":
            print("in here you need do the bubble sort")
            #bubble sort and output!!!!!

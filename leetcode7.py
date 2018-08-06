class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(x>2**31-1 or x<-1*2**31):
            return 0
        d=0
        num=0
        if(x>0):
            w=1
            z=x
            r=x
        else:
            w=-1
            z=-x
            r=-x
        print(r)
        while r>0.9:
            num+=1
            r=int(r/10)
        for i in range(num):
            print(num-i-1)
            d+=(z%10)*(10**(num-i-1))
            z=(z-z%10)/10
        if(int(d*w)>2**31-1 or int(d*w)<-1*2**31):
            return 0
        return int(d*w)
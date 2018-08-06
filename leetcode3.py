class Solution:
    def isrepeat(self, s):
        j = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if (s[j] == s[i]):
                    return True
        return False

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxnum = 1
        i = 0
        while i < len(s)-1:
            start = s[i]
            # print(start)
            # print(i)
            w = i
            for j in range(w + 1, len(s)):
                start += s[j]
                print(start)
                print(i)
                print("maxnum:"+str(maxnum))
                # print(start)
                # print("is repeat: "+str((self.isrepeat(start))))
                if (self.isrepeat(start)):
                    #print(len(start))
                    i += 1
                    break
                else:
                    # print(start)
                    maxnum = max(maxnum, len(start))
                    i += 1
        if (s!= ""):
            print(maxnum)
            return maxnum

        return 0

s1=Solution()

num=s1.lengthOfLongestSubstring("abcdefgabc")
print(num)
print(len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"))
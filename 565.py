class Solution:
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = 10
        s = [i for i in range(0, N + 1)]
        print(s)
        res = [None] * (len(s) + 1)
        res[1] = [1]
        num = 2
        s[1] = 0
        while num <= len(s) - 1:
            if s[num] == 0:
                num += 1
                continue
            else:
                start = num
                print("in")
                res[num] = [s[num]]
                s[num] = 0
                start += num
                while start < len(s):
                    res[num].append(s[start])
                    s[start] = 0
                    start += num
                num += 1

        print(res)


"""
for i in s:
            if i==num:
                s.append([s[num]])
            elif i%num==0:
                s[-1].append(num)
"""


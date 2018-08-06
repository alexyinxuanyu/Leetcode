class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums==[]:
            return 0
        i=0
        while i< len(nums)-1:#find the
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
                continue
            i+=1
        return len(nums)

nums=[1,1,2]
s=Solution()
s.removeDuplicates(nums)
print(nums)
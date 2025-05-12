class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        k = 0
        for i in range(length):
            if nums[i] == val:
                nums[i] = 101
                k += 1
        nums.sort()
        return length - k
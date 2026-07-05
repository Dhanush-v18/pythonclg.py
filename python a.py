class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # k tracks where to place the next unique number
        k = 1
        
        # Start from index 1 since the first element is always unique
        for i in range(1, len(nums)):
            # If the current number is different from the last unique one,
            # it's a new unique number
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k

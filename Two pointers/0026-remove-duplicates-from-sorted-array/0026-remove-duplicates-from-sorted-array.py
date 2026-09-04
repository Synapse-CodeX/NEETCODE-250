class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1,len(nums)):
            if(nums[r]==nums[r-1]):
                r+=1
            else:
                nums[l]=nums[r]
                l+=1
                r+=1
        return l
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
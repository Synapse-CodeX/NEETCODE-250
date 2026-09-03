class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n-1
        result = 0
        while i<j:
            area = (j-i)*min(heights[i],heights[j])
            result = max(area,result)
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return result

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
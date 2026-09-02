class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ''
        for c in s:
            if c.isalnum():
                newstr += c.lower()
        return newstr == newstr[::-1]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
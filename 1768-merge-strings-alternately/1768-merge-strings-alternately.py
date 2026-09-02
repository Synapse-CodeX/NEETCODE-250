class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0
        j = 0
        n = len(word1)
        m = len(word2)
        while(i<n and j<m):
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        result.append(word1[i:])
        result.append(word2[j:])
        return ''.join(result)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
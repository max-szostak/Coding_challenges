"""
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.
"""

class Solution:
    def minSwaps(self, data) -> int:
        numones = sum(data)
        if numones == 1:
            return 0
        currentones = maxones = sum(data[:numones])
        for i in range(numones, len(data)):
            removed = data[i - numones]
            if data[i] != removed:
                currentones += -1 if removed else 1
            maxones = max(currentones, maxones)
        return numones - maxones

sol = Solution()
print(sol.minSwaps([1,0,1,0,1,0,0,1,1,0,1]))
                
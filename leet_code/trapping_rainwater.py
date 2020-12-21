""" Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining. """

class Solution:
    def trap(self, height):
        lmaxes, rmaxes = [], []
        hmax = 0
        for h in height:
            if h > hmax:
                hmax = h
            lmaxes.append(hmax)
        hmax = 0
        for h in reversed(height):
            if h > hmax:
                hmax = h
            rmaxes.append(hmax)
        rmaxes.reverse()
        combined = [min(lmaxes[i], rmaxes[i]) for i in range(len(height))]
        water = 0
        for i in range(len(height)):
            water += combined[i] - height[i]
        return water

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
class Solution:
    def trap(self, height: List[int]) -> int:
        max_l, max_r = [], []
        water = curr_l = curr_r = 0


        max_l.append(0)
        for i in range(1, len(height)):
            curr_l = max(curr_l, height[i - 1])
            max_l.append(curr_l)
        
        max_r.append(0)
        for i in range(len(height) - 2, -1, -1):
            curr_r = max(curr_r, height[i + 1])
            max_r.append(curr_r)
        
        for i in range(len(height)):
            min_c = min(max_l[i], max_r[len(height) - 1 - i])
            curr_w = min_c - height[i]
            if curr_w > 0:
                water += curr_w
        
        return water
        
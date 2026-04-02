class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        l_max, r_max = height[left], height[right]
        water = 0

        while left < right:
            if l_max < r_max:
                left += 1
                l_max = max(l_max, height[left])
                water += l_max - height[left]
            else:
                right -= 1
                r_max = max(r_max, height[right])
                water += r_max - height[right]
                
        return water
        
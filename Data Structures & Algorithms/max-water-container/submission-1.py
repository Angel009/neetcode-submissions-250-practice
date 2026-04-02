class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area, left, right = 0, 0, len(heights) - 1

        while left < right:
            height = min(heights[left], heights[right])
            area = max(area, height * (right - left))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return area

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_deque = deque()
        min_deque = deque()
        max_len = 0

        for right in range(len(nums)):
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit:
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                
                left += 1
            
            max_len = max(max_len, right - left + 1)
        
        return max_len
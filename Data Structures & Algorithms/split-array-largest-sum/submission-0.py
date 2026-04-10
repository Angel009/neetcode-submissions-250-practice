class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        min_n, max_n = max(nums), sum(nums)
        ans = max_n

        while min_n <= max_n:
            mid = (min_n + max_n) // 2

            groups = 1
            curr_sum = 0

            for n in nums:
                if curr_sum + n > mid:
                    groups += 1
                    curr_sum = n
                else:
                    curr_sum += n
            
            if groups <= k:
                ans = mid
                max_n = mid - 1
            else:
                min_n = mid + 1
        
        return ans
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        ans = 0
        counter = 0

        for right in range(len(arr)):
            counter += arr[right]

            if right - left + 1 == k:
                if counter / k >= threshold:
                    ans += 1
                counter -= arr[left]
                left += 1
        
        return ans
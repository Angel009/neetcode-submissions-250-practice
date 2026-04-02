class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        arr = []
        ans = []

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        
        for key, val in frequency.items():
            arr.append([val, key])
        
        arr.sort()

        while len(ans) < k:
            ans.append(arr.pop()[1])
        
        return ans
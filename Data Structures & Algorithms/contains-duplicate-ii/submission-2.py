class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        uniques = set()
        for right in range(len(nums)):
            
            if right - left > k:
                uniques.remove(nums[left])
                left += 1
            
            if nums[right] in uniques:
                return True
            
            uniques.add(nums[right])
        
        return False
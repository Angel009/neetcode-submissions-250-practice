class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def mergeHelp(nums1, nums2):
            i, j =  0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    merged_nums.append(nums1[i])
                    i += 1
                else:
                    merged_nums.append(nums2[j])
                    j += 1
            merged_nums.extend(nums1[i:])
            merged_nums.extend(nums2[j:])
        
        ans = 0
        merged_nums = []
        
        mergeHelp(nums1, nums2)

        l_merged = len(merged_nums)

        if l_merged % 2 == 0:
            ans = (merged_nums[l_merged // 2] + merged_nums[(l_merged // 2) - 1]) / 2
        else:
            ans = merged_nums[l_merged // 2]
        
        return ans
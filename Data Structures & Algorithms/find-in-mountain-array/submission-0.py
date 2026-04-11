class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        len_m = mountainArr.length()

        low, high = 0, len_m - 1
        while low < high:
            mid = (low + high) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
            
        peak = low

        def binary_help(left, right, target, going_up):
            while left <= right:
                mid = (left + right) // 2
                val = mountainArr.get(mid)

                if val == target:
                    return mid
                
                if going_up:
                    if val < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    if val > target:
                        left = mid + 1
                    else:
                        right = mid - 1
            return -1

        ans = binary_help(0, peak, target, True)

        if ans != -1:
            return ans
        
        return binary_help(peak + 1, len_m - 1, target, False)
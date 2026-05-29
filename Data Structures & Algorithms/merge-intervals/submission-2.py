class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_interval = intervals[i]

            if ans[-1][1] >= curr_interval[0]:
                if ans[-1][1] < curr_interval[1]:
                    ans[-1][1] = curr_interval[1]
            
            else:
                ans.append(curr_interval)
        
        return ans
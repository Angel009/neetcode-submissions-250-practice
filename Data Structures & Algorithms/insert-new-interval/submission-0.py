class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []

        for i in range(len(intervals)):
            curr_interval = intervals[i]

            if newInterval[1] < curr_interval[0]:
                new_intervals.append(newInterval)
                return new_intervals + intervals[i:]

            elif newInterval[0] > curr_interval[1]:
                new_intervals.append(curr_interval)

            else:
                newInterval = [min(newInterval[0], curr_interval[0]),
                max(newInterval[1], curr_interval[1])]
        
        new_intervals.append(newInterval)

        return new_intervals
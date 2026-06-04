"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ans, count = 0, 0
        
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        p_s, p_e = 0, 0

        while p_s < len(intervals):
            if start[p_s] < end[p_e]:
                p_s += 1
                count += 1
            else:
                p_e += 1
                count -= 1
            ans = max(ans, count)
        
        return ans
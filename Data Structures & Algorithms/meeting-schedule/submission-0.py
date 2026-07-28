"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedInterval = sorted(intervals, key=(lambda x: x.start))

        for i in range(len(intervals)-1):
            current = sortedInterval[i]
            nextt = sortedInterval[i+1]
            if(nextt.start < current.end):
                return False

        return True

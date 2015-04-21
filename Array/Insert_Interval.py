Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        result = []
        n = len(intervals)
        if intervals == []: 
            result.append(newInterval)
            return result 
            # Can not return result.append(newInterval) directly !!!
        i = 0 
        
        while i < n and intervals[i].end < newInterval.start:
            result.append(intervals[i])
            i += 1
        
        if i == n:
            result.append(newInterval)
            return result 
        
        newstart = min(intervals[i].start, newInterval.start)
        # Here we decide the newstart for the newnode, nextstep is decide the end
        # But we need to skip to add the duplicate node like
        # [[1,5]], [2,3] --> [[1,5]], should not be [[1,5],[1,5]]
        # following code which is wrong !!
        # while i < n and intervals[i].end < newInterval.end:
        #     i += 1
        
        # if i < n:
        #     newend = max(intervals[i].end, newInterval.end)
        # else:
        #     newend = newInterval.end
        # result.append(Interval(newstart, newend))
        # note, the newend initialization: corner case: [[1,5]] [0,0]
        newend = newInterval.end
        while i < n and intervals[i].start <= newInterval.end:
            newend = max(intervals[i].end, newInterval.end)
            i += 1
        
        result.append(Interval(newstart, newend))   
        while i < n:
            result.append(intervals[i])
            i += 1
        return result 

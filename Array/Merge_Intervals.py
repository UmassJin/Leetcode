'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18]. 
'''

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        length = len(intervals)
        if length == 0 or length == 1: return intervals 
        intervals.sort()
        result = []
        pre = intervals[0]
        
        for i in xrange(1,length):
            flag = False
            if intervals[i].start > pre.end:
                result.append(pre)
            else:
                newnode = Interval(pre.start, max(intervals[i].end,pre.end))   
                # Wrong!! Here we did not handle the case: [1,8],[2,5],[3,6],[4,7],[5,9]!!
                result.append(newnode)
                flag = True
            pre = intervals[i]
        if not flag:
            result.append(pre)    
        return result 

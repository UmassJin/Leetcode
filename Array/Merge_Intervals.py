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
        if length == 0 or length == 1: 
            return intervals 
        intervals.sort(key = lambda x:x.start)
        result = []
        pre_start = None
        pre_end = None 
        
        for node in intervals:
            if pre_start == None and pre_end == None:
                pre_start = node.start
                pre_end = node.end 
            else:  
                if node.start <= pre_end:
                    if node.end > pre_end:
                        pre_end = node.end
            
                if node.start > pre_end:
                    newnode = Interval(pre_start, pre_end)
                    result.append(newnode)
                
                    pre_start = node.start
                    pre_end = node.end 
        
        newnode = Interval(pre_start, pre_end)    
        result.append(newnode)
        return result   


# Wrong Answer !!!
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

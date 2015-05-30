Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {Point[]} points
    # @return {integer}
    def maxPoints(self, points):
        if not points: return 0
        if len(points) < 3: return len(points)
        result = 0
        
        for point1 in points:
            samepoint = 1  # samepoint 初始化为1，算上自己的这个点
            table = {}
            table['inf'] = 0

            for point2 in points:
                if point1 == point2:
                    continue 
                else:
                    if point1.x == point2.x and point1.y != point2.y:
                        table['inf'] += 1
                    elif point1.x != point2.x:
                        k = 1.0 * (point1.y - point2.y) / (point1.x - point2.x)
                        if k not in table:
                            table[k] = 1
                        else:
                            table[k] += 1
                    else:
                        samepoint += 1
        
            result = max(result, max(table.values()) + samepoint)  
        
        return result 


# 注意考虑几点：
# 1) 相同的点个数，same points
# 2) 计算slope的时候用k = 1.0 * (points[i].y-points[j].y)/(points[i].x-points[j].x)
# 3) 考虑 x2 - x1 == 0 的情况，slope为'inf'
# 4) 思路是以一个点为中心，

'''
Write a function that takes the following inputs and gives the following outputs.

Input: A list of points in 2-dimensional space, and an integer k
Output: The k input points closest to (5, 5), using Euclidean distance

Example:
Input: {(-2, -4), (0, 0), (10, 15), (5, 6), (7, 8), (-10, -30)}, k = 2
Output: {(5, 6), (7, 8)}
'''

import heapq

def closet_points(array, target, k):
    if not array or len(array) < k:
        return array
    n = len(array)
    heap = []
    for point in array:
        dis = cal_distance(point, target)
        heap.append((dis, point))
    heapq.heapify(heap)
    result = []
    for _ in xrange(k):
        result.append(heapq.heappop(heap)[1])
        heapq.heapify(heap)
    return result
    
def cal_distance(p, q):
    return (p[0] - q[0])**2 + (p[1] - q[1])**2


test = [(-2, -4), (0, 0), (10, 15), (5, 6), (7, 8), (-10, -30)]
print closet_points(test, (5,5), 2)
~                                    


```python
import heapq
def merge_karray(lists):
    heap = []
    k = len(lists)
    result = []
    for i in xrange(k):
        heap.append((lists[i][0],i,0))

    heapq.heapify(heap)
    while heap:
        node = heapq.heappop(heap)
        value = node[0]
        row = node[1]
        cal = node[2]
        result.append(value)
        if cal + 1 < len(lists[row]):
            heapq.heappush(heap, (lists[row][cal+1], row, cal+1))
    return result

test = [[1,3,5],[2,4,6,8],[0,9,11,12]]
print merge_karray(test)
```

* heapq.heapify(a) 把list a中元素调换顺序使其成为最小堆, a还是list
* heapq.heappush(a, (10, sth_else))  把(10, sth_else)插入堆a中, a仍为最小堆, 也可以只插入数10
* heapq.heappop(a) 弹出堆顶元素, a中的最小值
* heapq.heappushpop(a, (10, sth_else)) 先push再pop, 效率比依次调用heappush()和heappop()高 

* Total time complexity:

        * Here, the heapiify use O(k), and then insert each number, each one use O(logk), totally use O(nlogk)
        * O(k + nlogk)

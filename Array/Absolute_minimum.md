[mitbbs](http://www.mitbbs.com/article_t/JobHunting/32782345.html) amazon interview 

Given three arrays A,B,C containing unsorted numbers. Find three numbers a, b, c from each of array A, B, C 
such that |a-b|, |b-c| and |c-a| are minimum Please provide as efficient code as you can.

Note: if a > b > c: |a-b| + |b-c| + |c-a| = 2(a-c) so this will always equals 2(max_num - min_num)

```python
import sys

def get_min_distance(A1, A2, A3):
    A1.sort()
    A2.sort()
    A3.sort()
    
    result = sys.maxint
    i1 = 0; i2 = 0; i3 = 0
    while True:
        minimum = min(A1[i1], A2[i2], A3[i3])
        maximum = max(A1[i1], A2[i2], A3[i3])
        result  = min(result, 2*(maximum-minimum))
        
        if result == 0: break
        if minimum == A1[i1] and i1<len(A1):
            i1 += 1
        elif minimum == A1[i2] and i2<len(A2):
            i2 += 1
        elif minimum == A3[i3] and i3<len(A3):
            i3 += 1
        else:
            break
    return result
    


```


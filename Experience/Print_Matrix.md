From [mitbbs](http://www.mitbbs.com/article_t/JobHunting/32570751.html) for Pinterest

Print a N x M matrix in diagonal from the upper left to lower right. 
However, with the following caveat. It's easy to just show the input and expect output.

```
matrix:
a b c d
e f g h
i j k l
m n o p

output:
a f k p
b g l
c h
d
e j o
i n
m
```

```python

def print_matrix(matrix):
    if not matrix: return None
    n = len(matrix)
    
    result = []
    for i in xrange(n):
        start = 0
        tmp_list = []
        while start + i < n:
            tmp_list.append(matrix[start][start+i])
            start += 1
        result.append(tmp_list)
        
    for i in xrange(1,n):
        tmp_list = []
        start = 0
        while start + i < n:
            tmp_list.append(matrix[start+i][start])
            start += 1
        result.append(tmp_list)
    return result

matrix = [['a','b','c','d'],['e','f','g','h'],['i','j','k','l'],['m','n','o','p']]
print print_matrix(matrix)

```

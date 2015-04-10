[G4G question](http://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/)
interview with facebook

```python
def findtrailzero(n):
    count = 0
    i = 5
    while n/i >= 1:
        count += n/i
        i *= 5
    return count

print "5: ",findtrailzero(5)
print "11: ",findtrailzero(11)
print "28: ",findtrailzero(28)
```

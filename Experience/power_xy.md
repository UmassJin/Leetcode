#### Write a program to calculate pow(x,n)
##### [G4G](http://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/)
##### [Facebook Interview](http://www.glassdoor.com/Interview/Implement-a-power-function-to-raise-a-double-to-an-int-power-including-negative-powers-QTN_137804.htm)

```python
# O(n)
def power(x, y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return  power(x, y/2)*power(x, y/2)
    else:
        return  x* power(x, y/2)*power(x, y/2)
        
#print power(2,5)
#print power(2,6)

# O(logn)

def power2(x, y):
    print "y: ", y
    if y == 0:return 1
    sign = 1
    if y < 0: sign = -1
    tmp = power2(x, abs(y)/2)
    if y % 2 == 0:
        tmp = tmp*tmp
    else:
        tmp = x*tmp*tmp
    if sign == -1:
        return 1.0/tmp
    else:
        return tmp
#print power2(2,6)
#print power2(2,7)
print power2(2,-2)
```

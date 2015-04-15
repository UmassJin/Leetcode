[G4G](http://www.geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character/)

O(n)

```python
# Note: count recort the char and count, order record the order of char 
def firstNonRep(istr):
    if not istr: return istr
    count = {}
    order = []
    for char in istr:
        if char not in count:
            count[char] = 1
            order.append(char)
        else:
            count[char] += 1
    for i in order:
        if count[i] == 1:
            return i
    return None

string = "geeksgeektoe"
print firstNonRep(string)
```

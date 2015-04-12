#####From mibbs for Linkedin Interview

Majority Element: A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).

Write a function which takes an array and emits the majority element (if it exists), otherwise prints NONE as follows:

```python
   I/P : 3 3 4 2 4 4 2 4 4
   O/P : 4

   I/P : 3 3 4 2 4 4 2 4
   O/P : NONE
```   

```python
def majority_number(A):
    candidate = None
    length  = len(A)
    count = 1

    for i in xrange(length):
        if candidate == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate = A[i]
            count = 1
    return candidate

def majority_number2(A):
    hashmap = {}
    length = len(A)
    result = None
    for i in xrange(length):
        if A[i] not in hashmap:
            hashmap[A[i]] = 1
        else:
            hashmap[A[i]] += 1
            if hashmap[A[i]] >= length/2:
                return A[i]
                break

test = [3,3,6,2,6,6,2,6,5]
test1 = [1,2,1,2,1,2,3,2,4,2]
print majority_number(test)
print majority_number2(test)
print majority_number(test1)
print majority_number2(test1)   

```

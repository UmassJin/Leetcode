Interview [mitbbs](http://www.mitbbs.com/article_t/JobHunting/32651839.html) for Groupon 

```python
def find_five(n):
    ret = []
    helper(ret, [], n)
    return ret

def helper(ret, res, n):
    if len(res) > 0 and ( int(''.join(res)) > n or len(res) > len(str(n)) ):
        #print "out, res: ", int(''.join(res))
        return
    if '5' in res and int(''.join(res)) not in ret:
        ret.append(int(''.join(res)))
        print "ret: ", ret

    for i in range(10):
        res.append(str(i))
        print "res: ", res
        helper(ret, res, n)
        res.pop()

print find_five(60)


```

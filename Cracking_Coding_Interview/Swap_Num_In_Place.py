'''
swap two numbers in place 
'''
# use bit manipulation 
# Or could use the diff 

def swap(a, b):
    print "before swap: a %d, b %d" %(a, b)
    a = a ^ b 
    b = a ^ b 
    a = a ^ b 
    print "after a: %d, b: %d" %(a, b)

swap(2,6)


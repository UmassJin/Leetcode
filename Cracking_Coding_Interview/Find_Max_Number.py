'''
Find the maximum of two numbers, should not use if-else or any other comparison operator 
'''

def flip(bit):
    return 1 ^ bit

def sign(a):
    return  flip((a >> 31) & 0x1)

# for positive, the sign bit is 0; for negative, the sign bit is 1
# here we transfer to: for positive, the sign bit is 1, for negative, the sign bit is 0

# Consider the over_flow scenario, if a = INT_MAX and b = -5 
# or a = INT_MIN and b = 5, a - b will over flow
# here consider the sign, if a*b < 0, has different sign, then use sign of a
# otherwise use the sign of c
def getmax(a, b):
    sa = sign(a)
    sb = sign(b)
    sc = sign(a-b)
    
    use_sign_a = sa ^ sb
    use_sign_c = flip(sa ^ sb)
    
    k = use_sign_a * sa + use_sign_c * sc
    q = flip(k)
    
    return k * a + q * b


print getmax(30,5)

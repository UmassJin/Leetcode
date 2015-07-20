'''
Write an algorithm that counts the number of ways you can paint a fence with N posts using K colors 
such that no more than 2 adjacent fence posts are painted with the same color.
# http://codereview.stackexchange.com/questions/63614/count-number-of-ways-to-paint-a-fence-with-n-posts-using-k-colors

The question asked for "an algorithm that counts the number of ways", so here's how I'd go about that.

I'll start with some notation. Assume that k is fixed. Then:

T(n) is the total number of ways to paint n fenceposts with k colours, 
subject to the constraint that no three adjacent posts are the same colour.
D(n) is the number of ways to paint n fenceposts with k colours such that the last two fenceposts are different colours (or n<2).
S(n) is the number of ways to paint n fenceposts with k colours such that the last two fenceposts are the same colour.

D(n)=(k−1)(D(n−1)+S(n−1)) for n≥2
S(n)=D(n−1) for n≥2
T(n)=D(n)+S(n)

==>
D(n)=(k−1)(D(n−1)+D(n−2)) for n≥3
T(n)=D(n)+D(n−1) for n≥2

==> 
D(n)=(k−1)(T(n−1)) for n≥3
and so:
T(n)=(k−1)(T(n−1)+T(n−2)) for n≥3

for example: have 3 colors, and n = 1:
T(1) = 3

for n = 2:
S(2): aa; bb; cc
D(2): ab; ac; ba; bc; ca; cb
T(2) = S(2) + D(2) = 3 + 6 = 9

for n = 3:
S(3): D(2), since we add one same char 
D(3): S(2) * (k-1) + D(2) * (k-1) = (k−1)(D(n−1)+S(n−1))

'''

def num_colors(n, k):
    if n <= 0 or k <= 0:
        return 0
    a = k
    b = k * k
    for i in xrange(n-1):
        a, b = b, (k-1)*(a + b)
    return a   # Note: here we need to return a 
            

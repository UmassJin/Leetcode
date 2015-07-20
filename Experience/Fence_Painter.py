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
            

'''
Similar question
第二轮是给一个int N，让输出所有的长度为N的valid string的个数，valid string的
定义是由A,B,C三种字母组成，并且在这个string中任意连续的三个字母不能包括A,B,C
三个字母，比如BACCA就不是valid string，因为前三个字母B,A,C包含了这三个字母。

假设dp_same[i]为长度=i+1，最后两位相同的valid string个数，dp_dif[i]为长度=i+1，最后两位不同的valid string个数。转移方程如下：
dp_same[i] = dp_same[i-1] + dp_dif[i-1]
dp_dif[i] = dp_same[i-1] * 2 + dp_dif[i-1]

dp_same[0] = 3
dp_dif[0] = 0

f(0): a; b; c
f(1) = dp_same[1] + dp_dif[1] 
f(1) means valid string number for string length is 2
aa; 
bb;
cc;
ab;
ac;
bc;
ba;
ca;
cb;

dp_same[3]: dp_same[2] + dp_diff[2]
dp_dif[3]: dp_same[2] * (k-1) + dp_dif[2]
f(3) = dp_same[3] + dp_dif[3]
'''

def valid_string(n):
    dp_same = 3
    dp_dif = 0
    
    for i in xrange(n-1):
        dp_same, dp_dif = dp_same+dp_dif, dp_same*2 + dp_dif
    return dp_same + dp_dif

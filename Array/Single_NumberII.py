Given an array of integers, every element appears three times except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one = 0; two = 0; three = 0
        for num in A:
            two |= one & num
            one = one ^ num
            three = one & two
            one = one & (~three)
            two = two & (~three)
        return one 
        
'''
Analysis:
The general idea of this problem, is to consider all the numbers bit by bit, count the occurrence of '1' in each bit. To get the result, check if the number can be divided by 3 (mod 3 = 0), put '0' if true and '1' otherwise.

(Idea coming from the internet)
Since we know that XOR operation can be used for testing if 1 bit occurs twice, in other words, for a single bit, if 1 occurs twice, it turns to 0. 
Now we need a 3-time criteria for each bit, by utilizing the bit operations.
This 3-time criteria needs every bit turns to 0 if  '1' occurs three times.

If we know on which bits '1' occurs twice, and also know on which bits '1' occurs 1-time, a simple '&' operation would result in the bit where '1' occurs three times. Then we turn these bit to zero, would do well for this problem.

(1). Check bits which have 1-time '1', use the XOR operation.
(2). Check bits which have 2-times '1's, use current 1-time result & current number.
(3). Check bits which have 3-times '1's, use '1-time' result & '2-times' result
(4). To turn 3-times bits into 0:   ~(3-times result) & 1-time result
                                                     ~(3-times result) & 2-times result
    
E.g.,We have numbers:  101101,   001100, 101010
To count the occurrence of 1's:
101101
001100
101010
count:  {2,0,3,2,1,1}

Denote:
t1: bit=1 if current bit has 1-time '1'
t2: bit=1 if current bit  has 2-times '1'
t3: bit=1 if current bit  has 3-times '1'

Result:
t1 = 000011, t2 = 100100, t3 = 001000



Initialization: t1 = 000000, t2=000000, t3 = 000000
(1) 101101
t1 = 101101  (using XOR)
t2 = 000000
t3 = 000000

(2)001100
% Current 2 times bits (t2) and NEW 2 times bits coming from 1 time bits and new number.
t2 = t2 | 001100 & t1 =  001100 & 101101 = 001100
t1 = t1 XOR 001100 = 100001
t3 = t2 & t1 = 000000

(3)101010
t2 = t2 | (101010 & t1) = t2 | (101010 & 100001) = 101100
t1 = t1 XOR 101010 = 100001 XOR 101010 = 001011

t3 = t1 & t2 = 001000

%Turn 3-time bits into zeros
t1 = t1 & ~t3 = 000011
t2 = t2 & ~t3 = 100100
'''

# Reference: http://yucoding.blogspot.com/2014/10/single-number-ii.html

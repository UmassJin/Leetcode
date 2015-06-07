'''
Easy Hash Function Show result 

14% Accepted
In data structure Hash, hash function is used to convert a string(or any other type) into an integer smaller than hash size 
and bigger or equal to zero. The objective of designing a hash function is to "hash" the key as unreasonable as possible. 
A good hash function can avoid collision as less as possible. A widely used hash function algorithm is using a magic 
number 33, consider any string as a 33 based big integer like follow:

hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE 

                              = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE

                              = 3595978 % HASH_SIZE

here HASH_SIZE is the capacity of the hash table (you can assume a hash table is like an array with index 0 ~ HASH_SIZE-1).

Given a string as a key and the size of hash table, return the hash value of this key.f



Have you met this question in a real interview? Yes
Example
For key="abcd" and size=100, return 78

Clarification
For this problem, you are not necessary to design your own hash algorithm or consider any collision issue, you just need to implement the algorithm as described.

'''


class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        if not key: return 0
        isum = 0
        
        magic_num = 1
        for char in key:
            number = ord(char)
            isum = (isum * 33 + number)%HASH_SIZE
        
        return isum 
    
  # 这里 (33*isum + number) --> 可能会超过 largest integer ! 需要每次HASH_SIZE, 得到最终的解
    
    def hashCode(self, key, HASH_SIZE):
        if not key: return 0
        ret = 0
        w = 1
        
        for i in xrange(len(key)-1, -1, -1):
            ret = (ret + ord(key[i]) * w)%HASH_SIZE
            w = (w * 33) % HASH_SIZE
        
        return ret            
    

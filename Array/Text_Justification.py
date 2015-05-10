Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' 
when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

click to show corner cases.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        cur_len = 0
        ret = []
        res = []
        
        for word in words:
            if cur_len + len(word) + len(res) <= L:  # Note 1
                cur_len += len(word)
                res.append(word)
            else:
                if len(res) == 1:
                    ret.append(self.fill_spaces(res[0],L)) # Note 7
                else:
                    extra_space = L - cur_len - (len(res)-1) # Note 2
                    each_extra = extra_space/(len(res)-1) + 1
                    rest_spaces = extra_space % (len(res)-1) # Note 8
                    for i in xrange(rest_spaces): # Note 3
                        res[i] += ' '
                    line = (' ' * each_extra).join(res)  ＃ Note 9
                    ret.append(line)
                res = []   # Note 4
                res.append(word) # Note 5
                cur_len = len(word)
        ret.append(self.fill_spaces(' '.join(res),L)) # Note 6
        return ret
    
    def fill_spaces(self, string, L):
        length = len(string)
        string += ' '* (L-length)
        return string 
                

# Notes:
# 1. 很好的思路，use cur_len + len(word) + len(res) 去判断
# 2. extra_space 去除了每个单词之间必须有的空格
#    each_extra 加上了每个单词之间必须有的空格
#    rest_spaces 除了每个单词之间必须有的空格和多余的空格，还剩下多少空格需要填补
# 3. 注意思想，如何加上多余的空格
# 4. after one loop, the res need to clean
# 5. Add the last word, for example here is "example", could not add into the first line,
#    add into the next line 
# 6. 最后是一定会append多余的一行的,没必要再check了, 直接append, 但是这里需要用
#    ' '.join, not the ''.join
# 7. 需要check长度为1，因为在下面计算中len(res)-1
# 8. 注意这里要用 extra_space去除以
# 9. 注意这里不能用以下的方法，会出现问题 ['a b ', 'c d ']，test case: ['a','b','c','d','e','f'], 3
#                   # substring = ''
                    # for ele in res:
                    #     substring += ele + ' '*each_extra 
                    # result.append(substring)
                    # 注意这里必须用join，不可以用循环，会出现['a b ','c d ']的情况

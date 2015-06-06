'''
Map_Reduce Example: count the numbers of occurrences of different words in a set of files 
'''
# word_count.py

import string
import map_reduce

'''
 input to a MapReduce job is just a set of (input_key, input_value) pairs
 In the wordcount example, the input keys will be the filenames of the files 
 we’re interested in counting words in, and the corresponding input values 
 will be the contents of those files.
'''

filenames = ["text/a.txt","text/b.txt","text/c.txt"]
i = {}
for filename in filenames:
    f = open(filename)
    i[filename] = f.read()
    f.close()

'''
The MapReduce job will process this input dictionary in two phases: 
the map phase, which produces output which (after a little intermediate processing) is then processed by the reduce phase.
In the map phase what happens is that for each (input_key,input_value) pair in the input dictionary i, 
a function mapper(input_key,input_value) is computed, whose output is a list of intermediate keys and values. 
'''
'''
 In the wordcount example, what mapper does is takes the input key and input value – 
 a filename, and a string containing the contents of the file – and then moves through 
 the words in the file. For each word it encounters, it returns the intermediate key and value (word,1), 
 indicating that it found one occurrence of word.
 '''
def mapper(input_key, input_value):
    return [(word,1) for word in remove_punctuation(input_value.lower()).split()]

''' test mapper
print mapper("text/a.txt", i['text/a.txt'])

Output:
[('the', 1), ('quick', 1), ('brown', 1), ('fox', 1), ('jumped', 1), ('over', 1), ('the', 1), ('lazy', 1), ('grey', 1), ('dogs', 1)]

After Mapper, we have this:
[('the', 1), ('quick', 1), ('brown', 1), ('fox', 1), 
 ('jumped', 1), ('over', 1), ('the', 1), ('lazy', 1), ('grey', 1), 
 ('dogs', 1), ('mary', 1), ('had', 1), ('a', 1), ('little', 1), 
 ('lamb', 1), ('its', 1), ('fleece', 1), ('was', 1), ('white', 1), 
 ('as', 1), ('snow', 1), ('and', 1), ('everywhere', 1), 
 ('that', 1), ('mary', 1), ('went', 1), ('the', 1), ('lamb', 1), 
 ('was', 1), ('sure', 1), ('to', 1), ('go', 1), ('thats', 1), 
 ('one', 1), ('small', 1), ('step', 1), ('for', 1), ('a', 1), 
 ('man', 1), ('one', 1), ('giant', 1), ('leap', 1), ('for', 1), 
 ('mankind', 1)]
'''

def remove_punctuation(s):
    return s.translate(string.maketrans("",""), string.punctuation)


"""
What the MapReduce library now does in preparation for the reduce phase is to group together all the 
intermediate values which have the same key. In our example the result of doing this is the following 
intermediate dictionary:
# in the code, this is the output of groups 

{'and': [1], 'fox': [1], 'over': [1], 'one': [1, 1], 'as': [1], 
 'go': [1], 'its': [1], 'lamb': [1, 1], 'giant': [1], 
 'for': [1, 1], 'jumped': [1], 'had': [1], 'snow': [1], 
 'to': [1], 'leap': [1], 'white': [1], 'was': [1, 1], 
 'mary': [1, 1], 'brown': [1], 'lazy': [1], 'sure': [1], 
 'that': [1], 'little': [1], 'small': [1], 'step': [1], 
 'everywhere': [1], 'mankind': [1], 'went': [1], 'man': [1], 
 'a': [1, 1], 'fleece': [1], 'grey': [1], 'dogs': [1], 
 'quick': [1], 'the': [1, 1, 1], 'thats': [1]}
 """

def reducer(intermediate_key,intermediate_value_list):
      return (intermediate_key,sum(intermediate_value_list))

"""
After Reducer, we have this
[('and', 1), ('fox', 1), ('over', 1), ('one', 2), ('as', 1), 
 ('go', 1), ('its', 1), ('lamb', 2), ('giant', 1), ('for', 2), 
 ('jumped', 1), ('had', 1), ('snow', 1), ('to', 1), ('leap', 1), 
 ('white', 1), ('was', 2), ('mary', 2), ('brown', 1), 
 ('lazy', 1), ('sure', 1), ('that', 1), ('little', 1), 
 ('small', 1), ('step', 1), ('everywhere', 1), ('mankind', 1), 
 ('went', 1), ('man', 1), ('a', 2), ('fleece', 1), ('grey', 1), 
 ('dogs', 1), ('quick', 1), ('the', 3), ('thats', 1)]
 """

 # map_reduce.py
'''
Defines a single function, map_reduce, which takes an input
dictionary i and applies the user-defined function mapper to each
(input_key,input_value) pair, producing a list of intermediate 
keys and intermediate values.  Repeated intermediate keys then 
have their values grouped into a list, and the user-defined 
function reducer is applied to the intermediate key and list of 
intermediate values.  The results are returned as a list.
'''
import itertools

def map_reduce(i,mapper,reducer):
   intermediate = []
   for (key,value) in i.items():
        intermediate.extend(mapper(key,value))
   groups = {}
    # very important step.
    # 1. lambda simply yields the first argument in the intermdediate, which is the key.
    #    That is used for setup group by what
    # 2. sorted is used to get the result grouped. See the later comment
    # 3. line 50 list comprehension is used to get the value, which can also use x[1] I think
   for key, group in itertools.groupby(sorted(intermediate), lambda x: x[0]):
        groups[key] = list([y for x, y in group])
    
   return [reducer(intermediate_key,groups[intermediate_key]) for intermediate_key in groups] 

 
 '''
 Map_Reduce Advantage
 You can probably already see how MapReduce takes advantage of a large cluster of computers, 
 but let’s spell out some of the details. There are two key points. First, the mapper functions can be run in parallel, 
 on different processors, because they don’t share any data. Provided the right data is in the local memory of the right 
 processor – a task MapReduce manages for you – the different computations can be done in parallel. The more machines are 
 in the cluster, the more mapper computations can be simultaneously executed. Second, the reducer functions can also be 
 run in parallel, for the same reason, and, again, the more machines are available, the more computations can be done 
 in parallel.
 
 '''
 
''' Additional Python library usage '''
# Note: the itertools.groupby usage  
# input: iterate input, like list, use the input function to group the list 

"""
from itertools import groupby
def groupby_even_odd(items):
    f = lambda x: 'even' if x % 2 == 0 else 'odd'
    gb = groupby(items, f)
    for k, items in gb:
        print '%s: %s' % (k, ','.join(map(str, items)))
>>> groupby_even_odd([1, 3, 4, 5, 6, 8, 9, 11])
odd: 1,3
even: 4
odd: 5
even: 6,8
odd: 9,11
Which is not what we want. To improve, simply do the following:
def groupby_even_odd(items):
    f = lambda x: 'even' if x % 2 == 0 else 'odd'
    gb = groupby(sorted(items, key=f), f)
    for k, items in gb:
        print '%s: %s' % (k, ','.join(map(str, items)))
>>> groupby_even_odd([1, 3, 4, 5, 6, 8, 9, 11])
even: 4,6,8
odd: 1,3,5,9,11
"""
 
 
 # Note the s.translate usage and string.maketrans, string.punctuation usage 
'''
string.translate(s, table[, deletechars])
Delete all characters from s that are in deletechars (if present), and then translate the characters using table, 
which must be a 256-character string giving the translation for each character value, indexed by its ordinal. 
If table is None, then only the character deletion step is performed.

>>> str = "2hel%^&lo,.$"
>>> str
'2hel%^&lo,.$'
>>> import string
>>> str.translate(string.maketrans("",""), string.punctuation)
'2hello'
'''




 
 
 
 
 

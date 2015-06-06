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
    return [(word,1) for word in remove_punctuation(inpu_value.lower()).split()]

def remove_punctuation(s):
    return s.translate(string.maketrans("",""), string.punctuation)

def reducer(intermediate_key,intermediate_value_list):
      return (intermediate_key,sum(intermediate_value_list))


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


 
 
 
 
''' Additional Python library usage '''
 
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




 
 
 
 
 

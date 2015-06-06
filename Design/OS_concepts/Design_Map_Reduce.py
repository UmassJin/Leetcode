'''
count the numbers of occurrences of different words
in a set of files 
'''

# input to a MapReduce job is just a set of (input_key, input_value) pairs
# In the wordcount example, the input keys will be the filenames of the files we’re 
# interested in counting words in, and the corresponding input values will be the contents of those files

filenames = ["text/a.txt","text/b.txt","text/c.txt"]
i = {}
for filename in filenames:
    f = open(filename)
    i[filename] = f.read()
    f.close()

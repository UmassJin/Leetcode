'''
I was given this problem in an interview. How would you have answered?

Design a data structure that offers the following operations in O(1) time:

insert
remove
contains
get random element


Consider a data structure composed of a hashtable H and an array A. The hashtable keys are the elements in the data structure, and the values are their positions in the array.

insert(value): append the value to array and let i be it's index in A. Set H[value]=i.
remove(value): We are going to replace the cell that contains value in A with the last element in A. let d be the last element in the array A at index m. let i be H[value], the index in the array of the value to be removed. Set A[i]=d, H[d]=i, decrease the size of the array by one, and remove value from H.
contains(value): return H.contains(value)
getRandomElement(): let r=random(current size of A). return A[r].
since the array needs to auto-increase in size, it's going to be amortize O(1) to add an element, but I guess that's OK.
'''

def __init__(self):
    self.dict = {}
    self.array = []
    self.size = 0

def insert(self, number):
    array.append(number)
    self.dict[number] = self.size
    self.size += 1

def remove(self, number):
    if self.contains(number):
      index = array.index(number)
      if index != len(self.array) - 1:
          hash[array[-1]] = index
          array[index], array[-1] = array[-1], array[index]
      del array[-1]
      del hash[number]
      self.size -= 1
    else:
      return False

def contains(self, number):
    if number not in self.dict.keys():
      return False
    else:
      return True 

def get_random_ele(self, index):
    if index < len(self.array):
        return self.array[index]
    else:
        return False 

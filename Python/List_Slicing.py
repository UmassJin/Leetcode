Array Slicing 

a[start:end] # items start through end-1
a[start:]    # items start through the rest of the array
a[:end]      # items from the beginning through end-1
a[:]         # a copy of the whole array
There is also the step value, which can be used with any of the above:

a[start:end:step] # start through not past end, by step
The key point to remember is that the :end value represents the first value 
that is not in the selected slice. So, the difference beween end and start is 
the number of elements selected (if step is 1, the default).

The other feature is that start or end may be a negative number, which means 
it counts from the end of the array instead of the beginning. So:
a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

The ASCII art diagram is helpful too for remembering how slices work:

 +---+---+---+---+---+
 | H | e | l | p | A |
 +---+---+---+---+---+
 0   1   2   3   4   5
-5  -4  -3  -2  -1

>>> seq[:]                # [seq[0],   seq[1],          ..., seq[-1]    ]
>>> seq[low:]             # [seq[low], seq[low+1],      ..., seq[-1]    ]
>>> seq[:high]            # [seq[0],   seq[1],          ..., seq[high-1]]
>>> seq[low:high]         # [seq[low], seq[low+1],      ..., seq[high-1]]
>>> seq[::stride]         # [seq[0],   seq[stride],     ..., seq[-1]    ]
>>> seq[low::stride]      # [seq[low], seq[low+stride], ..., seq[-1]    ]
>>> seq[:high:stride]     # [seq[0],   seq[stride],     ..., seq[high-1]]
>>> seq[low:high:stride]  # [seq[low], seq[low+stride], ..., seq[high-1]]

array = [1,2,3,4,5,6]
array[start:end:step]

>>> array[::1]
[1, 2, 3, 4, 5, 6]
>>> array[::2]
[1, 3, 5]
>>> array[::3]
[1, 4]
>>> array[0::3]
[1, 4]
>>> array[0::2]
[1, 3, 5]
>>> array[1::2]
[2, 4, 6]
>>> array[-1]
6
>>> array[-2:]
[5, 6]
>>> array[:-2]
[1, 2, 3, 4]


# CTCI
'''
from random5 to get random7
'''

import random

def rand5():
    return random.randint(0,4)

def rand7():
    num = 5 * rand5() + rand5()
    print num
    if num < 21:
        return num % 7

print rand7()


'''
Google Interview
from random2 to get random6
'''

# 思路:这道题的核心是保证产生random的概率一样，比如random7，则每个数字0到6产生的概率都为1/7,
# 对于random5来说，我们通过5*random5 + random5产生数字 0到24，然后取最小的3*7=21，所以取20
# 再mod7, 这里我们可以将random2先产生random4，然后通过random4产生

import random

def rand2():
    return random.randint(0,1)

def rand6():
    rand4 = 2*rand2() + rand2() 
    num = 4 * rand4 + rand4 # 0 to 9
    if num < 12:
        return num % 6

print rand6()

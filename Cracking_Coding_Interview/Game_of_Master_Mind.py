class Result:
    def __init__(self):
        self.hit = 0
        self.pseudohit = 0

def estimate(guess, solution):
    if len(guess) != len(solution): return None
    result = Result()
    idict = {}
    for i, char in enumerate(guess):
        if char == solution[i]:
            result.hit += 1
        else:
            idict[solution[i]] = idict.get(solution[i], 0) + 1   # Note: here we use the idict to record the solution frequency!
            
    for i, char in enumerate(guess):
        print "char: %s", char
        print "solution: ", solution
        if (char != solution[i]) and (idict.get(char, 0) > 0):
            result.pseudohit += 1
            idict[char] -= 1
            
    print "hit: %d, pseudohit: %d" %(result.hit, result.pseudohit)
    return result

guess = 'GGRR'
solution = 'RGGY'
estimate(guess, solution)

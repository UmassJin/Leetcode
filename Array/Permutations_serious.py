I) Permutations
Given a collection of numbers, return all possible permutations.
For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        result = []
        result_list = []
        result.append(num)
        self.Permutation(num, result, result_list)
        return result

    def Permutation(self, num, result, result_list):
        if len(num) == 2:
            result_list.append(num[1])
            result_list.append(num[0])
            result.append(result_list)
            return

        for i in range(len(num)):
            temp_list =[]
            if i != len(num) -1:
                temp = num[0:i] + num[i+1:]
            else:
                temp = num[0:i]
            temp_list = result_list + [num[i]] + temp
            if temp_list not in result:
                result.append(temp_list)
            self.Permutation(temp, result, result_list + [num[i]])
    
    # Recursion
    # Idea is first ele = 1, self.permute([2,3]) --> return ([2,3],[3,2])
    # Then get ([1,2,3],[1,3,2])
    # next ele = 2, self.permute([1,3]) --> return ([1,3],[3,1])
    # Then get([2,1,3],[2,3,1])
    # so far so forth, we could get the result 
    def permute(self, num):
        if len(num) <= 1: return [num]
        result = []
        for idx, ele in enumerate(num):
            for element in self.permute(num[:idx]+num[idx+1:]):
                result.append([ele] + element)
        return result 
    
    # Random generate (very slow!!)
    def permute(self, num):
        import random
        import math
        result = []
        length = len(num)
        total = math.factorial(length)
        while len(result) != total:
            a = random.sample(num,length)
            if a not in result:
                result.append(a)
        return result
        
    # Iteration 
    # input = [1,2,3]
    # i = 1 --> [[1]]
    # i = 2 --> [2,1],[1,2]
    # i = 3 --> [3,2,1],[2,3,1],[3,1,2],[1,3,2],[2,1,3],[1,2,3]
        def permute(self, num):
            result = [[]]
            permutations = []
            for i in num:
                if result == [[]]:
                    result = [[i]]
                else :
                    for j in result :
                        for k in range(0,len(j)+1) :
                            temp = j[:]
                            temp.insert(k,i)
                            permutations.append(temp)
                    result = permutations[:]
                    permutations = []
            return result

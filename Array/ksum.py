class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        def ksum(num, k, target):
            i = 0
            if k == 2:
                j = len(num)-1
                while i < j:
                    if num[i] + num[j] == target:
                        yield (num[i],num[j])
                        i += 1
                        #j -= 1
                        #while j > i and num[j] == num[j+1]: j-=1
                        #while i < j and num[i] == num[i-1]: i+=1
                    elif num[i] + num[j] > target:
                        j -= 1
                        #while j > i and num[j] == num[j+1]: j-=1
                    else:
                        i += 1
                        #while i < j and num[i] == num[i-1]: i+=1
            else:
                while i < len(num)-k+1:
                    newtarget = target - num[i]
                    for ele in ksum(num[i+1:], k-1, newtarget):
                        yield (num[i],) + ele  # here we need add ',' after num[i], which means tuple!!
                    i +=1
                    
        return [list(j) for j in set(ksum(num, 4, target))]
    
  # 注意yield的用法！

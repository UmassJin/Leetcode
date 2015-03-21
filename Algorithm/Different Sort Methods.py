A) Insertion Sort:
1. Efficient algorithm for sorting a small number of elements and nearly sort
2. Sort the array in-order
3. Invariant: everything to left is already sorted 
4. Runtime: worest-case: O(n^2) consider reverse-sorted input 
            best-case: O(n) consider the sorted input
Pseudocode:
  for i in xrange(1,len(array)):
    tmp = array[i]; 
    j = i - 1
    while j >= 0 and array[j] > tmp:
      A[j+1] = A[j]
      j -= 1
    A[j+1] = tmp

B) Merge Sort:
1. Divide, Conquer, Combine 
2. Runtime: O(nlogn)

Merge Part code:
    def merge(self, A, m, B, n):
        i = m-1; j = n-1; k = m+n-1
        
        while i >= 0 and j>=0:
            if A[i]>B[j]: A[k]=A[i];i-=1
            else: A[k]=B[j];j-=1
            k-=1
        
        if i<0:
            while j>=0:
                A[k]=B[j]
                j-=1;k-=1
        
        if j<0:
            while i>=1:
                A[k]=A[i]
                i-=1;k-=1


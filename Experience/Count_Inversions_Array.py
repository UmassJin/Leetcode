'''
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j

Example:
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
'''

# Note: G4G Analysis (http://www.geeksforgeeks.org/counting-inversions/)
def count_inver(A):
    if not A: return A
    length = len(A)
    return merge_sort(A, 0, length-1)


def merge_sort(A, left, right):
    inver_cnt = 0
    if left < right:
        mid = (left + right)/2
        inver_cnt = merge_sort(A, left, mid)
        inver_cnt += merge_sort(A, mid+1, right)
        inver_cnt += merge(A, left, mid+1, right)
    return inver_cnt

def merge(A, left, mid, right):
    i = left; j = mid; k = left
    print "i: %d, mid: %d, j: %d, k: %d, right: %d" %(i, mid, j, k, right)
    inver_cnt = 0
    tmp = [0 for p in xrange(len(A))]
    print "tmp: ", tmp
    while (i < mid) and (j <= right):
        print "A[i]: %d, A[j]: %d" %(A[i], A[j])
        if A[i] <= A[j]:
            tmp[k] = A[i]
            i += 1
            k += 1
            print "< after: i: %d, j: %d, k: %d, right: %d" %(i, j, k, right)
        else:
            tmp[k] = A[j]
            j += 1
            k += 1
            print "> after: i: %d, j: %d, k: %d, right: %d" %(i, j, k, right)
            inver_cnt += mid - i
    print "inver_cnt: ", inver_cnt

    while i < mid:
        tmp[k] = A[i]
        i += 1
        k += 1

    while j <= right:
        tmp[k] = A[j]
        j += 1
        k ++ 1

    A[left:right+1] = tmp[left:right+1]
    print "after merge: A", A
    return inver_cnt

ilist = [2,4,5,1,3,5]
print count_inver(ilist)

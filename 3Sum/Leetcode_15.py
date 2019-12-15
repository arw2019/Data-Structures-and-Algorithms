class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()
        res = []
        for i in range(len(A)-2):
            if i == 0 or (i > 0 and A[i]!=A[i-1]):
                lo, hi, tot = i+1, len(A)-1, 0-A[i]
                while lo < hi:
                    if A[lo] + A[hi] == tot:
                        res += [[A[i], A[lo], A[hi]]]
                        while lo < hi and A[lo] == A[lo+1]: lo += 1
                        while lo < hi and A[hi-1] == A[hi]: hi -= 1
                        lo += 1
                        hi -= 1 
                    elif A[lo] + A[hi] < tot:
                        while lo < hi and A[lo] == A[lo+1]: lo += 1
                        lo += 1
                    else:
                        while lo < hi and A[hi-1] == A[hi]: hi -= 1
                        hi -= 1
        return res

# Valid Mountain Array

'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < A[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
   Hide Hint #1  
It's very easy to keep track of a monotonically increasing or decreasing ordering of elements. You just need to be able to determine the start of the valley in the mountain and from that point onwards, it should be a valley i.e. no mini-hills after that. Use this information in regards to the values in the array and you will be able to come up with a straightforward solution.
'''

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        
        inc = False
        dec = False
        peak = False
        
        for i in range(1, n):
            if not peak:
                
                if arr[i]<arr[i-1]:
                    if inc:
                        peak = True
                    else:
                        return False
                    
                elif arr[i] == arr[i-1]:
                    return False
                
                else:
                    inc = True
                    
            if peak:
                
                if arr[i] == arr[i-1]:
                    return False
                
                elif arr[i]>arr[i-1]:
                    return False
                
                else:
                    dec = True
                
        return inc and dec and peak
                
        
class Solution2(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
            

# Min Cost Climbing Stairs

'''

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
   Hide Hint #1  
Say f[i] is the final cost to climb to the top from step i. Then f[i] = cost[i] + min(f[i+1], f[i+2]).

'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = [-1 for i in range(n+1)]
        
        def recur(i):
            
            if i <=1:
                return 0
            
            if dp[i]!=-1:
                return dp[i]
            
            else:
                
                j1 = cost[i-1]+recur(i-1)
                j2 = cost[i-2]+recur(i-2)
                
                dp[i] =  min(j1, j2)
                
                return dp[i]
            
        return recur(n)

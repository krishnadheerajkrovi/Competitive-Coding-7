"""
Approach 1:
1. The player 1 can pick either the leftmost or rightmost number from the array. 
2. When the player 1 picks a number, the player 2 will also pick max of the leftmost or rightmost number from the remaining array. 
3. So we see repeating patterns in the choices of the players. Hence recursion. 
4. We maximize the score gap between player 1 and player 2 by computing the score gap for both the choices of player 1 and taking the maximum of the two.

TC: O(n^2) 
SC: O(n^2) -> dp table

Approach 2:
1. We can store the score gap in 1d array
2. We start by computing the score gap for the subarrays of length 2 and then use that to compute the score gap for subarrays of length 3 and so on.
3. At end of round 1, we will have the score gap for the entire array in dp[0]

TC: O(n^2)
SC: O(n) -> dp array
"""

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        dp_table = collections.defaultdict(int)
        N = len(nums)

        def pick_optimal(nums,left,right):

            # Edge case- if only one element is left
            if left == right:
                return nums[left]
            
            # Check if the case has already been tackled before
            if (left,right) in dp_table:
                return dp_table[(left,right)]
            
            #We are concentrating on P1's score
            #Maximize the score gap between P1 and P2
            # When P1 picks left, it is assumed P2 will pick the max out of left+1 and the right
            # When P1 picks right, P2 will pick max of left and right-1

            case1 = nums[left] - pick_optimal(nums,left+1,right)
            case2 = nums[right] - pick_optimal(nums,left,right-1)

            #Store the choice that gives us the maximum score gap in the defaultdict
            dp_table[(left,right)] = max(case1,case2)

            return dp_table[(left,right)]
        
        return pick_optimal(nums,0,N-1) >= 0 
    

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]
        
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(nums[left] - dp[left + 1], nums[right] - dp[left])
        
        return dp[0] >= 0
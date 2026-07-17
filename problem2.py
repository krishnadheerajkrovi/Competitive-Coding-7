"""
1. Each number is the sum of the two numbers before it.
2. We can use recursion to calculate the nth number in the fibonacci sequence.

TC: O(2^n)
SC: O(n) -> recursion stack

Approach 2:
1. There are repeating subproblems, so we use cache.

TC: O(n)
SC: O(n) -> cache array
"""

    
class Solution:
    # Approach 1
    def fib(self, n: int) -> int:
        
        def fibonacci(n):
            if n==0:
                return 0 
            elif n==1 :
                return 1
            return fibonacci(n-1) + fibonacci(n-2)
        
        return fibonacci(n)

    # Approach 2
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        cache = [0] * (n + 1)
        cache[1] = 1

        for i in range(2, n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]

        return cache[n]

        
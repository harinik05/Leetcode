class Solution:
    def hammingWeight(self, n: int) -> int:
        counterOfOnes = 0
        while n!=0:
            counterOfOnes+=1
            n&=(n-1)
        return counterOfOnes
            
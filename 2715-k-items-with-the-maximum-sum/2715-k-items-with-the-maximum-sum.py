class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        if k <= numOnes:
            return k
        if k <= numOnes + numZeros:
            return numOnes
        k -= (numOnes + numZeros)

        return numOnes - (numNegOnes - (numNegOnes - k))


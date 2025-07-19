class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = Counter(deck).values()
        def _gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        gcd = -1
        for val in counter:
            if gcd == -1:
                gcd = val
            else:
                gcd = _gcd(gcd, val)

        if gcd >= 2:
            return True

        return False
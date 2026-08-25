class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0

        for i in range(32):
            x = (a >> i) & 1
            y = (b >> i) & 1
            z = (c >> i) & 1

            if z == 0:
                # Both x and y must be 0
                ans += x + y
            else:
                # At least one of x or y must be 1
                if x == 0 and y == 0:
                    ans += 1

        return ans        
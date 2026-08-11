class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = 0
        highest = 0

        for g in gain:
            altitude += g
            highest = max(highest, altitude)

        return highest      
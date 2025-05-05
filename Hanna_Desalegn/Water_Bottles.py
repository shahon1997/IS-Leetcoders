class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        empty = numBottles

        while empty >= numExchange:
            newfull = empty // numExchange
            total += newfull
            empty = empty % numExchange + newfull
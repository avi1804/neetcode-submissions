class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_needed(speed:int) -> int:
            return sum(math.ceil(pile/speed)for pile in piles)

        left , right = 1 , max(piles)
        result = right 

        while left <= right:
            mid = left + (right - left) // 2

            if hours_needed(mid) <= h:
                result = mid 
                right = mid - 1
            else:
                left = mid + 1

        return result
    
        
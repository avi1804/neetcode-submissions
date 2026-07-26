class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left , right = 0 , len(heights) -1 
        max_area = 0 

        while left < right:
            width = right - left 
            current_height = min (heights[left] , heights[right])
            max_area = max(max_area , width * current_height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
        
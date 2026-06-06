class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left,right=0,n-1
        final=0
        while left < right:
            curr=0
            curr=(right-left)*min(heights[left],heights[right])
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
            final=max(curr,final)
        return final
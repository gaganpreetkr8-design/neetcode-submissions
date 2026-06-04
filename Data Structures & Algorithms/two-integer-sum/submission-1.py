class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check =0
        ans=[]
        for i in range(len(nums)):
            check = target-nums[i]
            ans.append(i)
            for j in range(i+1,len(nums)):
                if nums[j]==check:
                    ans.append(j)
                    return ans
            ans.pop()
        return ans
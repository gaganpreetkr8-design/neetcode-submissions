class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=(sorted(nums))
        n=len(nums)
        final_res=[]
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target=0-nums[i]
            j,k=i+1,n-1
            while j < k:
                if nums[j]+nums[k]==target:
                    final_res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1] :
                        j+=1
                elif nums[j]+nums[k]>target:
                    k -=1
                else:
                    j+=1
                
        return final_res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        candidates.sort()
        def dfs(i,sub,total):
            if total==target:
                return res.append(sub.copy())

            for j in range(i,len(candidates)):    
                if j > i and candidates[j]==candidates[j-1]:
                    continue
                if total+candidates[j]>target:
                    break
                sub.append(candidates[j])
                dfs(j+1,sub,total+candidates[j])
                sub.pop()

        dfs(0,[],0)
        return res
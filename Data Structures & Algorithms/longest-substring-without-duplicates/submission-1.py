class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        curr_set=set()
        res=0
        for i in range(len(s)):
            while s[i] in curr_set:
                curr_set.remove(s[l])
                l += 1
            curr_set.add(s[i])
            res=max(res,i-l+1)
        return res
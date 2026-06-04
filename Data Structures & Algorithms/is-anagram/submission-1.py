class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hash_s={}
        hash_t={}
        for i in range(0,len(s)):
            if s[i] in hash_s:
                hash_s[s[i]] += 1
            else:
                hash_s[s[i]]=1
        for i in range(0,len(t)):
            if t[i] in hash_t:
                hash_t[t[i]] += 1
            else:
                hash_t[t[i]]=1
        if hash_s==hash_t:
            return True
        return False
        
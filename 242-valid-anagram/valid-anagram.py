class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i in t:
            if i in freq:
                freq[i]-=1
            else:
                return False

        for value in freq.values():
            if value!=0:
                return False
        return True
            

        
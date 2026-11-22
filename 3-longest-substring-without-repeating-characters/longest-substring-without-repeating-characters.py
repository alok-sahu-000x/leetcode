class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''n=len(s)
        if n==0:
            return 0
        ans =1
        set1=set({})
        set1.add(s[0])
        i = 0
        j=1
        while j < n:
            while s[j] in set1:
                set1.discard(s[i])
                i+=1
            set1.add(s[j])
            j+=1
            ans=max(ans,(j-i))
        return ans'''
        last_seen = {}
        left = 0
        max_len = 0
        
        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1
            else:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
            last_seen[char] = right
            
        return max_len




        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        #freq={}
        #for i in s:
         #   if i not in freq:
          #      freq[i]=1
           # else:
            #    freq[i]+=1
        #for i in range (len(s)):
         #   if freq[s[i]]==1:
          #      return i
        #return -1


        res = len(s)
        for ch in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(ch)
            if i != -1 and i == s.rfind(ch):
                if i < res:
                    res = i
        return res if res != len(s) else -1


            



        


        
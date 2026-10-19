class Solution:
    def twoSum(self, num: list[int], target: int) -> list[int]:
        #dict1 = {}
        #for i in range (len(num)):
         #   rem=target-num[i]
          #  if rem in dict1:
           #     return dict1[rem]+1,i+1
            #dict1[num[i]]=i
        left=0
        right=len(num)-1
        while left < right:
            sum1=num[left]+num[right]
            if sum1==target:
                return [left+1,right+1]
            elif sum1>target:
                right-=1
            else:
                left+=1
        
                





        
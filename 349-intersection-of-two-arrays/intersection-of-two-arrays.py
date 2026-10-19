class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1=set(nums1)
        res=set()
        for i in nums2:
            if i in set1:
                res.add(i)
        return list(res)
        
       # return list(set(nums1) & set(nums2))
        
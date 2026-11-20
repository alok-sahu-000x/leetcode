
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        mp = {}
        
        # Store strings and their indexes from list1
        for i, s in enumerate(list1):
            mp[s] = i

        min_sum = float('inf')
        result = []

        # Check common strings in list2
        for j, s in enumerate(list2):
            if s in mp:
                index_sum = mp[s] + j

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [s]

                elif index_sum == min_sum:
                    result.append(s)

        return result

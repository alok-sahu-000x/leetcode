from typing import List


class Solution:


    def plusOne(self, digits: List[int]) -> List[int]:
    # Traverse the list from right to left
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
    # If the digit is 9, it becomes 0 and the carry continues
            digits[i] = 0

    # If all digits were 9 (e.g., [9, 9] -> [0, 0]), prepend 1
        return [1] + digits

        
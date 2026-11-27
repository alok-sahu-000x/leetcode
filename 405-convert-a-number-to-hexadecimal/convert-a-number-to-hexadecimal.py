
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = ""

        num = num & 0xFFFFFFFF

        while num > 0:
            remainder = num & 15
            result = hex_chars[remainder] + result
            num >>= 4

        return result

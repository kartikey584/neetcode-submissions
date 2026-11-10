class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        count = {}
        result = 0

        for right in range(len(s)):

            char = s[right]

            count[char] = count.get(char, 0) + 1

            window_length = right - left + 1
            max_freq = max(count.values())

            replacements = window_length - max_freq

            if replacements > k:

                left_char = s[left]

                count[left_char] -= 1

                left += 1

            result = max(result, right - left + 1)

        return result
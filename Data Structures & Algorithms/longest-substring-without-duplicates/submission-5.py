class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        last_seen = {}
        left = 0
        result = 0

        for right in range(len(s)):

            char = s[right]

            if char in last_seen:
                left = max(left, last_seen[char] + 1)

            last_seen[char] = right

            result = max(result, right - left + 1)

        return result
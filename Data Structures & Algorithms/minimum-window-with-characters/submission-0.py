class Solution:
    def minWindow(self, s: str, t: str) -> str:

        left = 0
        seen = Counter(t)
        have = 0
        check = {}
        result = ""
        result_l = float("inf")

        for right in range(len(s)):

            char = s[right]
            check[char] = check.get(char,0) + 1

            if char in seen and check[char] == seen[char]:
                have += 1

            while have == len(seen):

                window_length = right - left + 1

                if window_length < result_l:

                    result_l = window_length
                    result = s[left:right+1]

                left_char = s[left]
                check[left_char] -= 1

                if left_char in seen.keys() and check[left_char] < seen[left_char]:
                    have -= 1
                
                left += 1

        return result
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = set()
        left = 0 
        res = 0

        for right in range(len(s)):
            while s[right] in last_seen:
                last_seen.remove(s[left])
                left += 1
            last_seen.add(s[right])
            res = max( res  ,  right - left + 1)
        return res
        
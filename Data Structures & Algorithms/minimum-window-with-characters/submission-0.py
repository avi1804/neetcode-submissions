class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = defaultdict(int)

        have , need_count = 0 , len(need)
        result , result_len = [-1,-1] , float("inf")
        left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] += 1

            if ch in need and window [ch] == need[ch]:
                have += 1

            while have == need_count:
                if (right - left + 1) < result_len:
                    result = [left , right]
                    result_len = right - left + 1

                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                left += 1

        left , right = result
        return s[left:right + 1] if result_len != float("inf") else ""

        
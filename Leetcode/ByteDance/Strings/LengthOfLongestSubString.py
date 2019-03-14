class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        special = []
        maxLen = 0
        for i in range(l):
            j = i
            while j < l:
                if s[j] not in special:
                    special.append(s[j])
                else:
                    break
                j += 1
            maxLen = max(maxLen, len(special))
            special.clear()
        return maxLen

so = Solution()
ml = so.lengthOfLongestSubstring("pwwkew")
print(ml)
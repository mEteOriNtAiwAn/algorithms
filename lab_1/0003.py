
def lengthOfLongestSubstring(s: str) -> int:
    if(len(s) == 0): return 0

    i = 0
    dict_ = dict()
    max_len = 0
    for k in range(len(s)):
        if s[k] in dict_ and dict_[s[k]] >= i:
            i = dict_[s[k]] + 1
        dict_[s[k]] = k
        max_len = max(max_len, k - i + 1)
    return max_len
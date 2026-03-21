def isPalindrome(s: str) -> bool:
        import re
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        i = 0
        k = len(s) - 1
        while(i < k):
            if s[i] != s[k]: return False
            i += 1
            k -= 1

        return True
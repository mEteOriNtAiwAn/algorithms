class Solution:     
    def generateParenthesis(self, n: int) -> list[str]:
        def recurison(left, right, s):
            if len(s) == n*2:
                result.append(s)
                return
            if left < n:
                recurison(left + 1, right, s + "(")
            
            if right < left:
                recurison(left, right + 1, s + ")")
            
        result = []
        recurison(0,0, "")
        return result
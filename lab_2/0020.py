class Solution:
    def isValid(self, s: str) -> bool:
        list_ = list()
        dict_ = {"{":"}", "(":")", "[":"]"}
        for ch in s:
            if ch in "{([":
                list_.append(ch)
            else:
                if(len(list_) == 0 or dict_[list_[-1]] != ch): return False
                list_.pop()
        
        if(len(list_) != 0): return False
        return True

        
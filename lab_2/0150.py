class Solution:
    def summ(self, a, b): return a + b
    def _summ(self, a, b): return a - b
    def multi(self, a, b): return int(a * b)
    def _multi(self, a, b): return int(a / b)

    def evalRPN(self, tokens: list[str]) -> int:
        if(len(tokens) == 1): return int(tokens[0])

        dict_func = {"+": self.summ, "-": self._summ, "*": self.multi, "/": self._multi}
        list_func = "+-*/"

        result = 0
        stec_number = []
        stec_func = []

        for i in range(len(tokens)):
            if tokens[i] in list_func:
                if(len(stec_number) >= 2):
                    b = stec_number.pop()
                    a = stec_number.pop()
                    
                    result = dict_func[tokens[i]](a,b)
                    stec_number.append(result)
                else:
                    stec_func.append(tokens[i])

            else:
                if(len(stec_func) >= 1 and len(stec_number) >= 1):
                    func = stec_func.pop()
                    a = stec_number.pop()

                    result = dict_func[func](a, tokens[i])
                    stec_number.append(result)
                else:
                    stec_number.append(int(tokens[i]))

        return result


        
            
        



class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator = {
            '+' : lambda a,b : a + b,
            '-' : lambda a,b : a - b,
            '*' : lambda a,b : a * b,
            '/' : lambda a,b : int(a/b)
        }
        for token in tokens:
            if token in operator:
                operand2 = stack.pop() #b
                operand1 = stack.pop() #a
                result = operator[token](operand1,operand2)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack.pop()
            

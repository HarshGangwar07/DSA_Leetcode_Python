class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #Only add open parentheses if open < n
        #Only add closing parentheses if close < open
        #Valid if closed == open == n
        
        stack = []
        res= []  #Stores valid parentheses

        def backtrack(OpenN, ClosedN):
            if OpenN == ClosedN == n:
                res.append("".join(stack))
                return
            
            if OpenN < n:
                stack.append("(")
                backtrack(OpenN + 1,ClosedN)
                stack.pop()
            
            if ClosedN < OpenN:
                stack.append(')')
                backtrack(OpenN, ClosedN + 1)
                stack.pop()
        
        backtrack(0,0)
        return res


        
        
from typing import List
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.floordiv,
    "*": operator.mul,
    }
# failed to solve
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(['+','-','*','/'])
        stack = []
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                num = stack.pop()
                if t == '+': stack[-1] += num
                elif t == '-': stack[-1] -= num
                elif t == '*': stack[-1] *= num
                else: stack[-1] = int(stack[-1]/num)
        return stack[-1]


tokens = ["2","1","+","3","*"]
x = Solution()
print(x.evalRPN(tokens))
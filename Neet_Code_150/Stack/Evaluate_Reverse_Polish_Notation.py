#Other way would be not pop two but only last element and perform the operation to the new last element

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        signs = ['+','-','*','/']
        for i in tokens:
            if i in signs:
                b = stack.pop(-1)
                a = stack.pop(-1)
                if i == '+':
                    stack.append(a+b) 
                elif i == '-':
                    stack.append(a-b) 
                elif i == '*':
                    stack.append(a*b) 
                elif i == '/':
                    stack.append(int(a/b))
            else:
                stack.append(int(i))

        return stack[0]
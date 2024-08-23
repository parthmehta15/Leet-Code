#Using Stack (Faster, More Memory)

class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        for i in s:
            if i == '(' or i =='[' or i == '{':
                curr.append(i)
            
            if i == ')':
                if len(curr) != 0 and curr.pop(-1) == '(':
                    continue
                else:
                    return False


            if i == '}':
                if len(curr) != 0 and curr.pop(-1) == '{':
                    continue
                else:
                    return False

            if i == ']':
                if len(curr) != 0 and curr.pop(-1) == '[':
                    continue
                else:
                    return False

        if curr == []:
            return True
        else:
            return False


# #Using String Manipulation (Slower, Less Memory)
# class Solution:
#     def isValid(self, s: str) -> bool:
#         while '()' in s or '[]' in s or '{}' in s:
#             s = s.replace('()','').replace('[]','').replace('{}','')
#         if s == '':
#             return True 
#         else:
#             return False
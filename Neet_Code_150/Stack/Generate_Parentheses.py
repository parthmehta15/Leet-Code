
#Final stack keep list of pattern and open and close count. Now if '(' then you can add '(' or ')'.
#Keep track of open and close bracket counts for each pattern. If open < close then can add anything.
#If open == close then can only add open. Also consider 0 count condition.

#New patterns are added in current stack and if no new pattern then return final_stack else copy curr_stack to final_stack.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        open_ = n-1
        close_ = n
        final_op = [['(',open_,close_]]
        curr_stack = []
        while True:
            # print('FInal',final_op)
            # print('curr',curr_stack)
            curr_stack = []
            for i in final_op:
                if i[1] == 0 and i[2] ==0:
                    continue
                if i[1] < i[2]:
                    if i[1]>0:
                        a = [i[0]+'(',i[1]-1,i[2]]
                        curr_stack.append(a)
                    b = [i[0]+')',i[1],i[2]-1]
                    curr_stack.append(b)
                elif i[1] == i[2]:
                    a = [i[0]+'(',i[1]-1,i[2]]
                    curr_stack.append(a)
            if curr_stack == []:
                break
            else:
                final_op = curr_stack[:]
                
        output = [i[0] for i in final_op]
        return output
                
        
            

                
            
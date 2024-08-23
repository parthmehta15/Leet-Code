# Have a output list of 0's
# Create a stack store both index and temp
# There can only be monotonically decreasing stack
# Loop through temperatures and if stack is not empty and while current temp is greater than last temp in stack 
# in the output pos at ind of stack temp store the differerence between curr index and stack ind
# Add the curr temp to stack (For the first values the above loop will be skipped)


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            # if len(stack) == 0 :
            #     stack.append([i, temp])
            while stack and temp>stack[-1][1]:
                ind, t = stack.pop()
                output[ind] = i - ind
            stack.append([i, temp])
        return output



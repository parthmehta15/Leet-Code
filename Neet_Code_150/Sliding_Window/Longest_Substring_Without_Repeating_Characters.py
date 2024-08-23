
# Change string into a list so easy to find idx
# Initialize curr_max , curr_list
# For i in the string list if it is not in curr_list then add to list and check the new len of list is greater than max length 
# If it is in the string then add to list and find the index of same element(python would give the idx of first instance then 
# re-assign list to the list[idx+1 : ], the size would definitely be reduced or remain the same size 



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = [*s]
        curr_max = 0
        curr_sub = []
        for i in range(len(data)):
            if data[i] in curr_sub:
                curr_sub.append(data[i])
                idx = curr_sub.index(data[i])
                curr_sub = curr_sub[idx + 1 :]
                
            else:
                curr_sub.append(data[i])
                curr_max = max(curr_max, len(curr_sub))
        
        return curr_max
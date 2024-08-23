
#Faster approach: 
# keep track of max_frequency element as well, but when we move start pointer to the right by 1,
# there is no need to reduce max+freq as we are finding the max_len anyway


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        data = {}
        start = 0
        max_len = 0
        max_freq = 0
        
        for end in range(len(s)):
            data[s[end]] = data.get(s[end],0) + 1
            max_freq = max(max_freq, data[s[end]])

            while (end - start + 1) - max_freq > k:
                data[s[start]] = data[s[start]] - 1
                start = start + 1
            max_len = max(max_len, end - start + 1)
        return max_len
    


# Slower Solution
# Initialize dictionary, start, end, max_len
# While end < len(str) 
# Add end to dictionary
# Now check if sum of all values - max value is <= k then 
# update max_len to sum of all elements and end = end + 1 and up
# else remove the start element from the list and start = start + 1 
# and end = end + 1
# return max_len

#TIP: this solution can be faster by replacing sum(data.values) with right - left, also no need to recalculate them


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        data = {}
        start = 0
        end = 0
        max_len = 0
        while end<len(s):
            data[s[end]] = data.get(s[end], 0 ) + 1
 
            if sum(data.values()) - max(data.values()) <=k:
                max_len = max(max_len,sum(data.values()))
                end = end + 1
            else:
                data[s[start]] = data.get(s[start], 0) - 1
                start = start + 1
                end = end + 1
        return max_len


# One soluton where I understood the problem incorrectly 
# Only thought you can go forward, but really liked the solution so here it is:

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         max_len = 0
#         data = [*s]
        
#         curr_k = k
#         curr_str = []
#         first_diff_letter = []
#         i = 0

        
#         while i< len(data):
#             print(i)
#             print(curr_str)
#             if curr_str == []:
#                 curr_str.append(data[i])
#                 max_len = max(max_len, len(curr_str))
#                 i = i +1

#             elif data[i] == curr_str[0]:
#                 curr_str.append(data[i])
#                 max_len = max(max_len, len(curr_str))
#                 i = i +1
            
#             elif data[i] != curr_str[0] and curr_k != 0:
#                 curr_str.append(data[i])
#                 max_len = max(max_len, len(curr_str))
#                 curr_k = curr_k - 1
#                 first_diff_letter.append((data[i], i))
#                 i = i +1

#             else:
#                 if first_diff_letter != []:
#                     curr_str = [first_diff_letter[0][0]]
#                     i = first_diff_letter[0][1] + 1
#                     curr_k = k 
#                     max_len = max(max_len, len(curr_str))
#                     first_diff_letter = []
#                 else:
#                     curr_str = [data[i]]
#                     i = i + 1
#                     max_len = max(max_len, len(curr_str))

#         return max_len

            



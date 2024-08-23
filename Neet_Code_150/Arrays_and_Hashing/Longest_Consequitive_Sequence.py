'''
Sort the element
The loop through only once due to O(n)
Define longest = 0 and curr_seq = []
Add first element to curr_seq list and change longest to 1
if same element is repeating: continue
if new element if 1 greater than the last element in curr_seq then append to curr_seq and update longest len
else maek curr_seq = [] and add element to it

'''



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 0
        curr_seq = []
        for i in nums:
            if curr_seq == []:
                curr_seq.append(i)
                if len(curr_seq) > longest:
                    longest = len(curr_seq)
                continue
            if i == curr_seq[-1]:
                continue
            if i == curr_seq[-1] + 1:
                curr_seq.append(i)
                if len(curr_seq) > longest:
                    longest = len(curr_seq)

            else:
                curr_seq = []
                curr_seq.append(i)
        
        return longest
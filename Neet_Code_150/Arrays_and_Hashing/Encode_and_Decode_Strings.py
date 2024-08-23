'''
Encode strings using their len, so str_len + '#' (a dellimiter mainly for strings with len greater than single digit) + str
Decode by looping and finding '#', changing values before that to int and ans then selecting that many numbers after the #, and append to output list
Keep track of index or update the encoded string
'''



class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        out = ''
        for i in strs:
            out = out + str(len(i)) + '#' + i
        return out
        

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        out = []
        while len(str)!= 0:
            for i in range(len(str)):
                if str[i] == '#':
                    break
            nums = int(str[:i])
            out.append(str[i+1:i+1+nums])
            str = str[i+1+nums:]
        return out
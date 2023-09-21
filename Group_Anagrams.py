
'''
Create a dict with key as the sorted str and value a list of anagrams
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = {}
        for i in strs:
            word = ''.join(sorted(i))
            if word in data:
                data[word].append(i)
            else:
                data[word] = [i]
        return list(data.values())
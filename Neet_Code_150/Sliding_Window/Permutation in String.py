
#Faster is to use dictionarys
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       
       if len(s1)>len(s2):
            return False
       s1_data = Counter(s1)
       s1_len = len(s1)
       s2_data = Counter(s2[:s1_len])
       if s1_data == s2_data:
                return True
       
       for i in range(len(s2)- len(s1)):
                s2_data[s2[i]] -= 1
                s2_data[s2[i+s1_len]] = s2_data.get(s2[i+s1_len], 0) + 1
                if s1_data == s2_data:
                    return True
       return False

#Slow solution
# loop thorugh s2 for size s2-s1 + 1 and if the element is in s2 then select substring of size s1
# compare if both are equal 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       
       s1_len =len(s1)

       for i in range(len(s2)- len(s1)+1):
            if s2[i] in s1:
                dummy = s2[i:i+s1_len]
                if sorted(dummy) == sorted(s1):
                    return True
       return False

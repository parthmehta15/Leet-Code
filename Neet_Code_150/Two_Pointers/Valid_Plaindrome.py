#Find all alphanumeric characters, convert to string, lower case and check if same as reverse string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x for x in s if x.isalnum()]).lower()
        if s == s[::-1]:
            return True
        else:
            return False
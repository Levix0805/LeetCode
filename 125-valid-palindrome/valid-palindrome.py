class Solution(object):
    def isPalindrome(self, s):
        self.s = s
        ls = s.lower().replace(" ","")
        clean_text = "".join(char for char in ls if char.isalnum())
        if clean_text == clean_text[::-1]:
            return  True
        return False

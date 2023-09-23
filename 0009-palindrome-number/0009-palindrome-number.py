class Solution(object):
    def isPalindrome(self, x):
        
        if x < 0:
            return False
        if x < 10:
            return True

        x_str = str(x)

        # Reverse the string and compare it to the original.
        return x_str == x_str[::-1]

##20250320##

class Solution:
    def isPalindrome(self, x: int) -> bool:
        list = str(x)
        if list == list[::-1]:
            return True
        else:
            return False


###test###

n = Solution()
print(n.isPalindrome(x = 121))
print(n.isPalindrome(x = -121))
print(n.isPalindrome(x = 10))


'''

###Sample###

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
        
'''

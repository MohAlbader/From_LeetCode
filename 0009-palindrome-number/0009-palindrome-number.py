import math
class Solution(object):
    def isPalindrome(self, x):
        xinitial = x
        if x<0 or x == 10:
            return False
        if 0<=x<10:
            return True
        digits = 1 + int(math.log10(x))
        newNum = 0
        for i in range(digits-1,-1,-1):
            newNum += (x % 10)*10**i
            x = x//10
        return newNum == xinitial
    
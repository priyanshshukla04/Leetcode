class Solution:

    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        if string[::-1] == string:
            return True
        else:
            return False
        # rev = 0
        # while x > 0:
        #     a = x % 10
        #     rev = rev * 10 + a
        #     x = x // 10
        # print(rev)
        # if rev == x:
        #     print("2")
        # else:
        #     print("3")


obj = Solution()
print(obj.isPalindrome(121))

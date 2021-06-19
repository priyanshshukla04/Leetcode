class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if(x>0):
            while (x > 0):
                a = x % 10
                rev = rev * 10 + a
                x = x // 10
            print("yegh",rev)
        elif(x<0):
            while (abs(x) > 0):
                a = abs(x) % 10
                rev = rev * 10 + a
                x = abs(x) // 10
            rev = -(rev)
            print("ggg",rev)
        if (pow(-2, 31) <= rev <= pow(2, 31) - 1):
            return rev
        else:
            return 0;

obj = Solution()
print(obj.reverse(-123))
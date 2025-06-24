# Sign of the product of an array
import math
class Solution:
    def sign(self,nums: list[int]):
        try:
            i = nums.index(0)
            if i:
                return 0
        except ValueError:
            if math.prod(nums) > 0:
                return 1
            else:
                return -1

if __name__ == "__main__": 
    s1 = Solution()
    print(s1.sign([-1,-2,-3,-4,3,2,1]))
    print(s1.sign([1,5,0,2,-3]))
    print(s1.sign([0,-61,26,-7,5,-54,-52,27,-92,-42,-81]))

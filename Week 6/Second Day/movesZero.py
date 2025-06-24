# Moves Zero
class Solution:
    def movesZero(self,nums: list[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            try:
                count = nums.count(0)
                while count > 0:
                    nums.remove(0)
                    nums.append(0)
                    count -= 1
            except ValueError:
                ...
        print(nums)

if __name__ == "__main__":
    s1 = Solution()
    s1.movesZero([0,1,0,3,12])
    s1.movesZero([0])
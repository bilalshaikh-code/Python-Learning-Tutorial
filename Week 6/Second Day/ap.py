#  arithmetic progression
class Solution:
    def  arithmeticProgression(self,arr: list[int]):
        arr.sort()
        arrProg = arr[1] - arr[0]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] != arrProg:
                return False
        return True

if __name__ == "__main__":
    s1 = Solution()
    print(s1.arithmeticProgression([3,5,1]))
    print(s1.arithmeticProgression([1,2,4]))
    # s1.arithmeticProgression([3,5,1])
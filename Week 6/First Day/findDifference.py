# Find the difference
class Solution:
    def findDifference(self,s: str,t: str):
        s1 = sorted(s)
        t1 = sorted(t)
        for i in range(len(s)):
            if s1[i] != t1[i]:
                return t1[i]
        return t1[len(t1)-1]

if __name__ == "__main__":
    s1 = Solution()
    print(s1.findDifference("abcd","abcde"))
    print(s1.findDifference("abcd","abycd"))
    print(s1.findDifference("","y"))
    print(s1.findDifference("abcd","abycd"))
    # print(s1.findDifference(input("s: "),input("t: ")))
# Repeated Substring Pattern
class Solution:
    def substring(self,s: str):
        return s in (s + s)[1:-1] #This code isn't my.

if __name__ == "__main__":
    s1 = Solution()
    print(s1.substring("abab"))
    print(s1.substring("aba"))
    print(s1.substring("abcabcabc"))
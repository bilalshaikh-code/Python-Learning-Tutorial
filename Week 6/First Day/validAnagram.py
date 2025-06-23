# Valid Anagram
class Solution:
    def anagram(self,s: str,t: str):
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
    
if __name__ == "__main__":
    s1 = Solution()
    print(s1.anagram("anagram","nagaram"))
    print(s1.anagram("rat","car"))
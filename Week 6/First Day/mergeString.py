# Merge String Alternately
class Solution:
    def mergeAlternately(self,word1: str,word2: str):
        merge = ""
        length = max(len(word1),len(word2))
        for i in range(length):
            if i < len(word1):
                merge += word1[i]
            if i < len(word2):
                merge += word2[i]
        print(merge)

if __name__ == "__main__":
    s1 = Solution()
    s1.mergeAlternately("abc","pqr")
    s1.mergeAlternately(word1 = "ab", word2 = "pqrs")
    s1.mergeAlternately( word1 = "abcd", word2 = "pq")
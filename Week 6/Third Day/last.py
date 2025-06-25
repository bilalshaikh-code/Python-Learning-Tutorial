# Length of last word
class Solution:
    def lastWord(self,s: str):
        i = -1
        while s.split(" ")[i] == "":
            # print(len(s.split(" ")[i]))
            i -= 1
            # print(i)
        print(len(s.split(" ")[i]))
        
if __name__ == "__main__":
    s1 = Solution()
    s1.lastWord("Hello World")
    s1.lastWord("   fly me   to   the moon  ")
    s1.lastWord("Luffy is still joyboy")
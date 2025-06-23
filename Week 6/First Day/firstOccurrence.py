# Find the index of the first occurrence in a string.
class Solution:
    def firstOccurrence(self,haystack: str,needle: str):
        return (haystack.find(needle))
    
if __name__ == "__main__":
    s1 = Solution()
    print(s1.firstOccurrence("sadbutsad","sad"))
    print(s1.firstOccurrence("leetcode","leeto"))
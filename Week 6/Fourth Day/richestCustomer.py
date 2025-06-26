# Richest Customer wealth
class Solution:
    def wealth(self,accounts: list[list[int]]):
        cus = []
        for i in accounts:
            total = 0
            for j in i:
                total += j
            cus.append(total)
        
        print(max(cus))

if __name__ == "__main__":
    s1 = Solution()
    s1.wealth([[1,2,3],[3,2,1]])
    s1.wealth([[1,5],[7,3],[3,5]])
    s1.wealth([[2,8,7],[7,1,3],[1,9,5]])
# Matrix to set Zeros
class Solution:
    def setZeros(self,matrix: list[list[int]]):
        co = 0
        for i in matrix:
            co += i.count(0)
        
        indexs = []
        for i in range(co):
            for j in matrix:
                try:
                    indexs.append(j.index(0))
                except ValueError:
                    ...
        print(indexs)

if __name__ == "__main__":
    s1 = Solution()
    # s1.setZeros([[1,1,1],[1,0,1],[1,1,1]])
    s1.setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]])
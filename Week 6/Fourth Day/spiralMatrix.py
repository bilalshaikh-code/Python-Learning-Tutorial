# Spiral Matrix
class Solution:
    def spiralMatrix(self,matrix: list[list[int]]):
        mlist = []
        i = 0
        while i < len(matrix):
            j = i
            while j < len(matrix[i]):
                mlist.append(matrix[i][j])

if __name__ == "__main__":
    s1 = Solution()
    s1.spiralMatrix([[1,2,3],[4,5,6],[7,8,9]])
    s1.spiralMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
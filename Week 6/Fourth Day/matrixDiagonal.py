# Matrix diagonal sum
class Solution:
    def matSum(self,mat: list[list[int]]):
        primary = 0
        if len(mat) > 1:
            for i in range(len(mat)):
                for j in range(len(mat[i])):
                    if i == j:
                        primary += mat[i][j]
                    elif (len(mat[i])-1) - i == j:
                        primary += mat[i][j]            
        else:
            primary = mat[0][0]
        print(primary)

if __name__ == "__main__":
    s1 = Solution()
    s1.matSum([[1,2,3],[4,5,6],[7,8,9]])
    s1.matSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]])
    s1.matSum([[5]])
    s1.matSum([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
    # print("[\n[1,1,1,1,1]\n[1,1,1,1,1]\n[1,1,1,1,1]\n[1,1,1,1,1]\n[1,1,1,1,1]\n]")
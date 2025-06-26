# Find the Tic Tac Toe Game Winner.
class Solution:
    def findWinner(self,moves: list[list[int]]):
        winnerPossiblity = [[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]],[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]]]

        payler_A = []
        payler_B = []
        i = 0
        while i < len(moves):
            try:
                payler_A.append(moves[i])
                payler_B.append(moves[i+1])
            except IndexError:
                ...
            i += 2
        for i in winnerPossiblity:
            print(i)

if __name__ == "__main__":
    s1 = Solution()
    print(s1.findWinner([[0,0],[2,0],[1,1],[2,1],[2,2]]))
    # print(s1.findWinner([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
    # print(s1.findWinner([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))
    # print(s1.findWinner([[0,0],[2,0],[1,1],[2,1],[1,1]]))
    # print(s1.findWinner([[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]]))
    # print(s1.findWinner([[1,2],[1,1],[0,2],[2,2],[2,1],[0,1],[0,0]]))
    # print(s1.findWinner([[2,0],[1,1],[0,2],[2,1],[1,2],[1,0],[0,0],[0,1]]))
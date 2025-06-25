# Robot return to origin
class Solution:
    def origin(self,moves: str):
        # up - , down - , right - , left - 
        # up = 0
        # dw = 0
        # rt = 0
        # lf = 0
        # for i in moves:
        #     if i == 'U':
        #         up += 1
        #     elif i == 'D':
        #         dw += 1
        #     elif i == 'R':
        #         rt += 1
        #     elif i == 'L':
        #         lf += 1
        # if up == dw and rt == lf:
        #     return True
        # else:
        #     return False
        print(f"{moves.count('U') == moves.count("D") and moves.count("R") == moves.count("L")}")

if __name__ == "__main__":
    s1 = Solution()
    s1.origin("UL")
    s1.origin("RLUURDDDLU")
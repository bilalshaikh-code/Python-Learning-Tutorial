# Roman to Integer
class Solution:
    def romanToInt(self,s: str):
        # s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
        num = 0
        for i in range(len(s)):
            if s[i] == "I":
                num += 1
            elif s[i] == "V":
                if s[i-1] == "I" and i-1 >= 0:
                    num += 5 - 2
                else:
                    num += 5
            elif s[i] == "X":
                if s[i-1] == "I" and i-1 >= 0:
                    num += 10 - 2
                else:
                    num += 10
            elif s[i] == "L":
                if s[i-1] == "X" and i-1 >= 0:
                    num += (50 - 20) 
                else:
                    num += 50
            elif s[i] == "C":
                if s[i-1] == "X" and i-1 >= 0:
                    num += (100 - 20)
                else:
                    num += 100
            elif s[i] == "D":
                if s[i-1] == "C" and i-1 >= 0:
                    num += (500 - 200)
                else:
                    num += 500
            elif s[i] == "M":
                if s[i-1] == "C" and i-1 >= 0:
                    num += (1000 - 200)
                else:
                    num += 1000
        return num

if __name__ == "__main__":
    s1 = Solution()
    print(s1.romanToInt("III"))
    print(s1.romanToInt("LVIII"))
    print(s1.romanToInt("MCMXCIV"))
    # print(s1.romanToInt(input("Enter roman number: ")))
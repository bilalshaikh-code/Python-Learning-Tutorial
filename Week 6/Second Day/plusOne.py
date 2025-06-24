# Plus One
class Solution:
    def plusOne(self,digits: list[int]):
        num = int(digits.__str__().replace(", ","").replace("[","").replace("]",""))
        num += 1
        for i in range(len(str(num))):
            try:
                digits[i] = int(str(num)[i])
            except IndexError:
                digits.append(int(str(num)[i]))
        print(digits)

if __name__ == "__main__":
    s1 = Solution()
    s1.plusOne([1,2,3])
    s1.plusOne([4,3,2,1])
    s1.plusOne([9])
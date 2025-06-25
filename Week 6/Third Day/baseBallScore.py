# Base Ball Score
class Solution:
    
    def isnumber(self,num: str):
        try:
            return int(num) > 0 or int(num) < 0
        except ValueError:
            return False

    def score(self,operations: list[str]):
        # 'C' is represent the previse score is invalid remove it.
        # 'D' previse score to double and add that as the new score.
        # '+' previse two score to add and add that as the new score.
        score = 0
        i = 0
        while i < len(operations):
            if operations[i] == 'C':
                j = i -1
                while not self.isnumber(operations[j]):
                    j -= 1
                score -= int(operations[j])
                operations.remove(operations[j])
                i -= 1
            elif operations[i] == 'D':
                j = i -1
                while not self.isnumber(operations[j]):
                    j -= 1
                score += (2*int(operations[j]))
                operations.insert(j+1,str(2*int(operations[j])))
                i += 1
            elif operations[i] == '+':
                j = i -1
                while not self.isnumber(operations[j]):
                    j -= 1
                k = j - 1
                while not self.isnumber(operations[k]):
                    k -= 1
                score += (int(operations[j])+int(operations[k]))
                operations.insert(j+1,str(int(operations[j])+int(operations[k])))
                i += 1
            else:
                score += int(operations[i])
            i += 1
        print(f"Score: {score}")

if __name__ == "__main__":
    s1 = Solution()
    # s1.score(["5","2","C","D","+"])
    s1.score(["5","-2","4","C","D","9","+","+"])
    s1.score(["1","C"])
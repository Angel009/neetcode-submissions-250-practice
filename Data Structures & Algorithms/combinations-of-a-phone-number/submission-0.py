class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

        ans = []

        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                ans.append(curr_str)
                return
            
            for c in letters[digits[i]]:
                backtrack(i + 1, curr_str + c)
        
        if digits:
            backtrack(0, "")
        
        return ans
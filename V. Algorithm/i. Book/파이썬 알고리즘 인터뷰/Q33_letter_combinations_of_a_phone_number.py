class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(idx, word):
            if len(word) == len(digits):
                words.append(word)
                return
            
            for i in range(idx, len(digits)):
                for j in table[digits[i]]:
                    dfs(i + 1, word + j)
                
            
        table = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'vwyz'
        }
        
        words = []
        word = ''
        dfs(0, '')
        return words

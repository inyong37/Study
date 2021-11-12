from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results
        
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        for idx, val in enumerate(expression):
            if val in "+-*":
                left = self.diffWaysToCompute(expression[:idx])
                right = self.diffWaysToCompute(expression[idx+1:])
                results.extend(compute(left, right, val))
        return results

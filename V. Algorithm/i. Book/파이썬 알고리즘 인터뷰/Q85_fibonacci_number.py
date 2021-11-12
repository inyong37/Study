class Solution:
    def fib(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y
        return x

'''
import collections


def fib(self, N: int) -> int:
  if N <= 1:
    return N
  return self.fib(N - 1) + self.fib(N - 2)


class Solution:
  dp = collections.defaultdict(int)
  
  def fib(self, N: int) -> int:
    if N <= 1:
      return N
    
    if self.dp[N]:
      return self.dp[N]
    self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
    return self.dp[N]
  
  
class Solution:
  dp = collections.defaultdict(int)

  def fib(self, N: int) -> int:
    self.dp[1] = 1

    for i in range(2, N + 1):
      self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
    return self.dp[N]

  
def fib(self, N: int) -> int:
  x, y = 0, 1
  for i in range(0, N):
    x, y = y, x + y
  return x


import numpy as np


def fib(n):
  M = np.matrix([[0, 1], [1, 1]])
  vec = np.array([[0], [1]])
  
  return np.matmul(M ** n, vec)[0]
'''

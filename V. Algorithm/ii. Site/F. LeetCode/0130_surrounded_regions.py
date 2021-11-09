# https://leetcode.com/problems/surrounded-regions/submissions/
# Solution 1st
from collections import Counter

class Solution:
    def __init__(self):
      self.op = str()
      self.op_op = str()
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if len(board) == 1 or len(board) == 2:
          return
        
        boarder = []
        for i in range(len(board)):
          for j in range(len(board[i])):
            if i == 0 and j == 0:
              pass
            elif i == 0 and j == len(board[i]) - 1:
              pass
            elif i == len(board) - 1 and j == 0:
              pass
            elif i == len(board) - 1 and j == len(board[i]) - 1:
              pass
            else:
              boarder.append(board[i][j])
        self.op = Counter(boarder).most_common(1)[0][0] # majority
        if self.op == 'O':
          self.op_op = 'X'
        else: # X
          self.op_op = 'O'
        
        def dfs(i, j, op, op_op):
          if i < 1 or i >= len(board) - 1 or j < 1 or j >= len(board[0]) - 1 or board[i][j] != op_op:
            return
          
          board[i][j] = op
          dfs(i, j + 1, op, op_op)
          dfs(i, j - 1, op, op_op)
          dfs(i + 1, j, op, op_op)
          dfs(i - 1, j, op, op_op)
          
        for i in range(len(board)):
          for j in range(len(board[i])):
            if board[i][j] == self.op_op: # O
              dfs(i, j, self.op, self.op_op)

# Solution 2nd
from collections import Counter

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i, j):
          if i < 1 or i >= len(board) - 1 or j < 1 or j >= len(board[0]) - 1 or board[i][j] != 'O':
            return
          
          board[i][j]  = 'X'
          dfs(i, j + 1)
          dfs(i, j - 1)
          dfs(i + 1, j)
          dfs(i - 1, j)
          
        for i in range(1, len(board) - 1):
          for j in range(1, len(board[i]) - 1):
            if board[i][j] == 'O':
              dfs(i, j)

# Solution 3rd
# Reference: https://zhenyu0519.github.io/2020/03/07/lc130/
# first find surrounded regions and mark them as 'visited',
# second flip others and make back marked regions.

from collections import Counter

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return board
        
        row, col = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        
        def dfs(x, y):
            for delta_x, delta_y in directions:
                new_x, new_y = x + delta_x, delta_y + y
                if 0 <= new_x and new_x <= row - 1 \
                and 0 <= new_y and new_y <= col - 1 \
                and board[new_x][new_y] == 'O' \
                and (new_x, new_y) not in visited:
                    visited.add((new_x, new_y))
                    board[new_x][new_y] = 'V'
                    dfs(new_x, new_y)
        
        for x in range(row):
            for y in range(col):
                if (x == 0 or x == row - 1 or y == 0 or y == col - 1) and \
                board[x][y] == 'O' and \
                (x, y) not in visited:
                    visited.add((x, y))
                    board[x][y] = 'V'
                    dfs(x, y)

        for x in range(row):
            for y in range(col):
                if board[x][y] == 'O':
                    board[x][y] = 'X'
                elif board[x][y] == 'V':
                    board[x][y] = 'O'

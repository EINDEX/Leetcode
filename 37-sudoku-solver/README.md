# Sudoku Solver

## Difficulty
Hard

## Question
<p>Write a program to solve a Sudoku puzzle by filling the empty cells.</p>

<p>A&nbsp;sudoku solution must satisfy <strong>all of&nbsp;the following rules</strong>:</p>

<ol>
	<li>Each of the digits&nbsp;<code>1-9</code> must occur exactly&nbsp;once in each row.</li>
	<li>Each of the digits&nbsp;<code>1-9</code>&nbsp;must occur&nbsp;exactly once in each column.</li>
	<li>Each of the the digits&nbsp;<code>1-9</code> must occur exactly once in each of the 9 <code>3x3</code> sub-boxes of the grid.</li>
</ol>

<p>Empty cells are indicated by the character <code>&#39;.&#39;</code>.</p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height:250px; width:250px" /><br />
<small>A sudoku puzzle...</small></p>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Sudoku-by-L2G-20050714_solution.svg/250px-Sudoku-by-L2G-20050714_solution.svg.png" style="height:250px; width:250px" /><br />
<small>...and its solution numbers marked in red.</small></p>

<p><strong>Note:</strong></p>

<ul>
	<li>The given board&nbsp;contain only digits <code>1-9</code> and the character <code>&#39;.&#39;</code>.</li>
	<li>You may assume that the given Sudoku puzzle will have a single unique solution.</li>
	<li>The given board size is always <code>9x9</code>.</li>
</ul>


## Solution
### python3
```python3
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[True for _ in range(9)] for _ in range(9)]
        cols = [[True for _ in range(9)] for _ in range(9)]
        boxs = [[True for _ in range(9)] for _ in range(9)]
        
        for x in range(9):
            for y in range(9):
                t = board[x][y]
                if t == '.':
                    continue
                t = int(t) - 1
                rows[x][t] = False
                cols[y][t] = False
                bid = x//3 + (y//3)*3
                boxs[bid][t] = False
                
        self.dfs(board, rows, cols, boxs)
        
    def dfs(self, board, rows, cols, boxs, x=0, y=0):
        while board[x][y] != '.':
            x += 1
            if x > 8:
                x = 0
                y += 1
            if y > 8:
                return True
        
        for k in range(9):
            bid = x//3 + (y//3)*3
            if rows[x][k] and cols[y][k] and boxs[bid][k]:
                board[x][y] = str(k+1)
                rows[x][k] = False
                cols[y][k] = False
                boxs[bid][k] = False
                if self.dfs(board, rows, cols, boxs, x, y):
                    return True
                else:
                    board[x][y] = '.'
                    rows[x][k] = True
                    cols[y][k] = True
                    boxs[bid][k] = True
                    
        return False
```

## Author
EINDEX
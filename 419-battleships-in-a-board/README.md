# Battleships in a Board

## Difficulty
Medium

## Question
Given an 2D board, count how many battleships are in it. The battleships are represented with <code>'X'</code>s, empty slots are represented with <code>'.'</code>s. You may assume the following rules:

<ul>
<li>You receive a valid board, made of only battleships or empty slots.</li>
<li>Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape <code>1xN</code> (1 row, N columns) or <code>Nx1</code> (N rows, 1 column), where N can be of any size.</li>
<li>At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.</li>
</ul>

<p><b>Example:</b><br />
<pre>X..X
...X
...X
</pre>
In the above board there are 2 battleships.

<p><b>Invalid Example:</b><br />
<pre>...X
XXXX
...X
</pre>
This is an invalid board that you will not receive - as battleships will always have a cell separating between them.
<p></p>
<p><b>Follow up:</b><br>Could you do it in <b>one-pass</b>, using only <b>O(1) extra memory</b> and <b>without modifying</b> the value of the board?</p>

## Solution
### python
```python
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for x,y in [ (x,y) for x in range(len(board)) for y in range(len(board[0]))][::-1]:
            if board[x][y] == 'X':
                if ((y > 0 and board[x][y-1] != 'X') or y == 0) and ((x > 0 and board[x-1][y] != 'X') or x == 0 ):
                    count += 1
        return count                
        
            
        

```

## Author
EINDEX
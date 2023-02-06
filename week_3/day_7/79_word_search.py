"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 
Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true


Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true


Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?

Link: https://leetcode.com/problems/word-search/

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW = len(board)
        COL = len(board[0])

        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == word[0] and self.helper(row, col, ROW, COL, board, word, 0):
                    return True

        return False

    def helper(self, row, col, ROW, COL, board, word, i):
        if i == len(word):
            return True

        if row in range(ROW) and col in range(COL) and board[row][col] == word[i]:
            temp = board[row][col]
            board[row][col] == "#"

            direction = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            for r, c in direction:
                if self.helper(r, c, ROW, COL, board, word, i+1):
                    return True
                
            board[row][col] = temp
            return False
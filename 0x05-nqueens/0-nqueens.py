#!/usr/bin/python3
"""
backtracking algorithm placing N non-attacking queens on an N×N chessboard
"""
import sys

if len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if not (num >= 4):
    print("N must be at least 4")
    sys.exit(1)


def solveNQueens(n):
    """Solve for n queens"""
    col = set()  # track used columns
    neg = set()  # (r - c) track used negative diagonals
    pos = set()  # (r + c) track used positive diagonals
    res = []
    # result

    board = [[] for n in range(n)]
    # create empty board

    def backtrack(row):
        """recursion fnct"""
        # on reaching last row
        if row == n:
            # copy of current solution
            copy = board.copy()
            res.append(copy)
            return

        for c in range(n):  # for columns
            # for used column or diagonals,skip
            if c in col or (row + c) in pos or (row - c) in neg:
                continue

            # track found columns and diagonals
            col.add(c)
            pos.add(row + c)
            neg.add(row - c)

            board[row] = [row, c]

            backtrack(row + 1)  # move to next row

            # handle undoing
            col.remove(c)
            pos.remove(row + c)
            neg.remove(row - c)
            board[row] = []

    backtrack(0)

    return res

if __name__ == "__main__":
    boards = solveNQueens(num)
    for board in boards:
        print(board)

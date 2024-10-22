#!/usr/bin/python3
"""The N queens puzzle is the challenge of placing N non-attacking queens 
on an N×N chessboard
 Write a program that solves the N queens problem
"""

import sys

def is_valid(board, row, col):
    """Check if a queen can be placed at board[row][col]"""
    for i in range(row):
        if board[i] == col:
            return False

    for i in range(row):
        if board[i] - i == col - row or board[i] + i == col + row:
            return False

    return True

def solve_nqueens(N, row, board, solutions):
    """Recursive function to solve the N Queens problem"""
    if row == N:
        solution = [[i, board[i]] for i in range(N)]
        solutions.append(solution)
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)

def nqueens(N):
    """Solve the N Queens problem and print all solutions"""
    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)

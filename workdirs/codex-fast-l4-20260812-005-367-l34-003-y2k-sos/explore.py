"""
Minimax solver for the SOS game on 1xn boards.
Value from current player's perspective: +1 = win, -1 = lose, 0 = draw.
"""
import sys
from functools import lru_cache

def solve(n):
    @lru_cache(maxsize=None)
    def value(board):
        filled = sum(1 for x in board if x != 0)
        if filled == n:
            return 0  # draw

        best = -2
        for i in range(n):
            if board[i] != 0:
                continue
            for letter in (1, 2):  # 1=S, 2=O
                new_board = board[:i] + (letter,) + board[i+1:]
                # check if this move creates SOS
                if creates_sos(new_board, i, n):
                    return 1  # current player wins immediately
                v = -value(new_board)
                if v > best:
                    best = v
                if best == 1:
                    return 1
        return best

    def creates_sos(board, pos, n):
        for start in range(max(0, pos - 2), min(n - 3, pos) + 1):
            if board[start] == 1 and board[start+1] == 2 and board[start+2] == 1:
                return True
        return False

    initial = tuple([0] * n)
    result = value(initial)
    states = value.cache_info().currsize
    return result, states

if __name__ == "__main__":
    for n in range(1, 13):
        val, states = solve(n)
        # val is from first player's perspective at the start
        # +1 = first player wins, -1 = second player wins, 0 = draw
        outcome = "P1 wins" if val == 1 else ("P2 wins" if val == -1 else "Draw")
        print(f"n={n:2d}: {outcome:10s}  (states={states})")

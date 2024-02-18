#!/usr/bin/python3
'''N Queens Interview Question'''
import sys


class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def get_input(self):
        """Retrieves and validates the program's argument.

        Returns:
            int: The size of the chessboard.
        """
        if len(sys.argv) != 2:
            self.exit_with_error("Usage: nqueens N")
        try:
            self.n = int(sys.argv[1])
        except ValueError:
            self.exit_with_error("N must be a number")
        if self.n < 4:
            self.exit_with_error("N must be at least 4")

    def exit_with_error(self, message):
        print(message)
        sys.exit(1)

    def is_attacking(self, pos0, pos1):
        """Checks if the positions of two queens are in an attacking mode.

        Args:
            pos0 (list or tuple): First queen's position.
            pos1 (list or tuple): Second queen's position.

        Returns:
            bool: True if the queens are in an attacking position
                  otherwise False.
        """
        return pos0[0] == pos1[0] or pos0[1] == pos1[1] or \
            abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])

    def group_exists(self, group):
        """Checks if a group exists in the list of solutions.

        Args:
            group (list of integers): A group of possible positions.

        Returns:
            bool: True if it exists, otherwise False.
        """
        for stn in self.solutions:
            i = sum(1 for stn_pos in stn if stn_pos in group)
            if i == self.n:
                return True
        return False

    def build_solution(self, row, group):
        """Builds a solution for the n queens problem.

        Args:
            row (int): The current row in the chessboard.
            group (list of lists of integers): The group of valid positions.
        """
        if row == self.n:
            tmp0 = group.copy()
            if not self.group_exists(tmp0):
                self.solutions.append(tmp0)
        else:
            for col in range(self.n):
                a = (row * self.n) + col
                matches = zip([pos[a]] * len(group), group)
                used_positions = map(lambda x:
                                     self.is_attacking(x[0], x[1]), matches)
                group.append(pos[a].copy())
                if not any(used_positions):
                    self.build_solution(row + 1, group)
                group.pop()

    def get_solutions(self):
        """Gets the solutions for the given chessboard size.
        """
        global pos
        pos = list(map(lambda x: [x // self.n, x % self.n],
                       range(self.n ** 2)))
        a = 0
        group = []
        self.build_solution(a, group)


if __name__ == "__main__":
    solver = NQueensSolver(0)
    solver.get_input()
    solver.get_solutions()
    for solution in solver.solutions:
        print(solution)

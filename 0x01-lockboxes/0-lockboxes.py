#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    numberOfBoxes = len(boxes)
    visitedBoxes = set()

    def dfs(idx):
        """Depth-first search"""
        if idx in visitedBoxes or idx >= numberOfBoxes or idx < 0:
            return
        visitedBoxes.add(idx)
        for key in boxes[idx]:
            dfs(key)

    dfs(0)
    return numberOfBoxes == len(visitedBoxes)

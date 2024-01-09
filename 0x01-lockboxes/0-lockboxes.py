#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    def dfs(box, visitedBox):
        """Depth First Search to traverse the boxes"""
        visitedBox[box] = True
        for key in boxes[box]:
            if not visitedBox[key]:
                dfs(key, visitedBox)

    numberOfBoxes = len(boxes)
    visitedBoxes = [False] * numberOfBoxes
    initialBox = 0

    dfs(initialBox, visitedBoxes)

    return all(visitedBoxes)

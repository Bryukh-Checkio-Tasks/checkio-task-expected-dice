"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

import random

TESTS = {
    "Basics": [],
    "Jumps": [],
    "Big": []
}

def addTest(c, i, a):
    TESTS[c].append({"input": i, "answer": a})

addTest("Basics", [1, 4, 1, [0, 0, 0, 0]], 4.00)
addTest("Basics", [1, 4, 2, [0, 0, 0, 0]], 4.00)
addTest("Basics", [1, 4, 3, [0, 0, 0, 0]], 4.00)
addTest("Basics", [1, 4, 3, [0, 2, 1, 0]], 1.33)
addTest("Basics", [1, 4, 3, [0, -1, -2, 0]], 4.00)
addTest("Basics", [1, 3, 3, [0, 0, 0, 0, 0]], 3.51)
addTest("Basics", [1, 6, 1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 8.57)
addTest("Basics", [2, 6, 1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 10.21)
addTest("Basics", [1, 10, 1, [0, 0, 0, 0, 0, 0, 0, 0]], 7.20)

addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 9.81)
addTest("Jumps", [1, 6, 9, [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]], 9.66)
addTest("Jumps", [1, 6, 9, [0, 2, 0, 0, 0, 0, 0, 0, 0, 0]], 8.48)
addTest("Jumps", [1, 6, 9, [0, 3, 0, 0, 0, 0, 0, 0, 0, 0]], 8.65)
addTest("Jumps", [1, 6, 9, [0, 2, 1, 0, 0, 0, 0, 0, 0, 0]], 7.66)
addTest("Jumps", [1, 6, 9, [0, 2, 2, 0, 0, 0, 0, 0, 0, 0]], 7.77)
addTest("Jumps", [1, 6, 9, [0, 2, 3, 0, 0, 0, 0, 0, 0, 0]], 7.75)
addTest("Jumps", [1, 6, 9, [0, 3, 1, 0, 0, 0, 0, 0, 0, 0]], 7.79)
addTest("Jumps", [1, 6, 9, [0, 3, 2, 1, 0, 0, 0, 0, 0, 0]], 8.00)
addTest("Jumps", [1, 6, 9, [0, 3, 3, 3, 0, 0, 0, 0, 0, 0]], 8.00)
addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, -1, 0]], 9.85)
addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, -2, 0]], 9.95)
addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, -3, 0]], 9.79)
addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, -7, 0]], 11.08)
addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 0, 0, 0, 0, -99, 0]], 5.16)
addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, 2, -2, 0, 0, 0, 0]], 9.77)
addTest("Jumps", [1, 6, 9, [0, 0, 0, 0, -2, 2, 0, 0, 0, 0]], 11.37)

addTest("Big", [1, 4, 29, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 29.60)
addTest("Big", [1, 6, 29, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 29.71)
addTest("Big", [3, 10, 29, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 30.00)
addTest("Big", [2, 6, 29, [0, -1, -2, -3, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 31.67)
addTest("Big", [2, 6, 29, [0, -2, -3, -4, -5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 5.70)
addTest("Big", [1, 6, 29, [0, -1, -2, -3, -4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 35.67)
addTest("Big", [1, 6, 29, [0, -2, -3, -4, -5, -6, -7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], 1.00)

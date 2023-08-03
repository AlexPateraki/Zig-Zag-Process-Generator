# Zig-Zag-Process-Generator
- Your program will start with a parent process at level 0 and will spawn (`fork`) 2 other child processes. The left child and the right child.
- These children will be at level 1. Only one of these two children will perform a fork. If the current level number is odd (1, 3, 5, 7, 9), only the left child will fork. Otherwise, only the right child will fork.

Specifications:
* The number of levels (zigzag steps) will be passed as a parameter from the command line during the execution of `zigzag.py`.
* The number of levels (zigzag steps) cannot exceed 10.
* Each forked process should print a message to the screen in the following format (PIDs are examples):
  * `I am process with PID = 11 standing at Level 1 of the zigzag path, my parent is PID=1002 and I am its left child`
  * `I am process with PID = 12 standing at Level 1 of the zigzag path, my parent is PID=1002 and I am its right child`
  * `...`

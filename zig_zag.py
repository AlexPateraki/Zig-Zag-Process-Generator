%%file zigzaggen.py

import os, sys

MAX_LEVEL = 10

def child_allowed_to_fork(level: int) -> str:
    """Decides which child is allowed to fork, based on given level
    """
    if level % 2 == 0:
        return "right"
    return "left"

def print_statement(current_level: int, position: str) -> None:
    """Prints each child's information according to the format given by the professor
    """
    print(f"I am process with PID = {os.getpid()} standing at Level {current_level+1} of the zig zag path, my parent is PID={os.getppid()} and I am its {position} child")

def get_input():
    number_of_levels = int(input("Please enter the desired number of levels (between 1 and 10): "))
    if number_of_levels not in range (1, MAX_LEVEL+1):
        print((f"Number of levels should be between 1 and {MAX_LEVEL}"))
        os._exit(1)
    return number_of_levels

def main():
    '''if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <number of levels>")
        os._exit(1)
    
    number_of_levels = int(sys.argv[1])
    
    if number_of_levels not in range (1, MAX_LEVEL+1):
        print((f"Number of levels should be between 1 and {MAX_LEVEL}"))
        os._exit(1)'''

    number_of_levels = get_input()
        
    for i in range(number_of_levels):
        print("\n\n")
        left = os.fork()
        if left == 0:
            print_statement(i, "left")
            if child_allowed_to_fork(i+1) == "left":
                continue
            else:
                os._exit(0) #?????
        elif left == -1:
            print(os.strerror("Failed to fork"))
            #os._exit(1)
        else:
            right = os.fork()
            if right == 0:
                print_statement(i, "right")
                if child_allowed_to_fork(i+1) == "right":
                    continue
                else:
                    os._exit(0) #?????
            elif right == -1:
                print(os.strerror("Failed to fork"))
                #os._exit(1)
            else:
                os.wait()
                os.wait()
            os._exit(0)
    return 0

if __name__ == '__main__':
    os._exit(main())

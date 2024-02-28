# This is a CLI tool to generate a fast world for the PGCL Library
import sys
import random

arguments = sys.argv

# The Idea when calling the tool is creating an array of arrays with the next structure
# [
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]   
# ]

def main():
    for arg in arguments:
        if arg == "--random":
            rows = random.randint(3, 20)
            cols = random.randint(3, 20)
            world = []
            for i in range(rows):
                row = []
                for j in range(cols):
                    if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                        block = 1
                    else:
                        block = random.randint(0, 1)
                    row.append(block)
                world.append(row)
                
            print(f"[RESULT]: \n {world}")
                    

if __name__ == "__main__":
    main()
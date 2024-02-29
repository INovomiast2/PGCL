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
        if "--random" in arguments:
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
        elif "-w" in arguments and "-h" in arguments:
            arg_index_w = arguments.index('-w')
            arg_index_h = arguments.index('-h')
            
            if arguments[arg_index_w + 1].isnumeric() and arguments[arg_index_h + 1]:
                rows = int(arguments[arg_index_w + 1])
                cols = int(arguments[arg_index_h + 1])
                world = []
                for i in range(rows):
                    row = []
                    for j in range(cols):
                        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                            block = 1
                        else:
                            block = 0
                        row.append(block)
                    world.append(row)
                print(f"[RESULT]: \n {world}")

if __name__ == "__main__":
    main()
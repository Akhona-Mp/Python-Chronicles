import sys

# To run : python3 {file name} {file you want to count lines}

"""
This program counts the amount of lines in a python file ,only the 
ones with code,comments are not counted.

"""

def main():
    file = sys.argv
    line_count = line_counter(file)
    print(line_count)

def line_counter(file):

    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit()

    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit()
    
    if ".py" not in sys.argv[1]:
        print("Not a Python file")
        sys.exit()
    
    try:
        with open(sys.argv[1],"r") as f:
            code = f.readlines()
    except FileNotFoundError:
        return "File does not exist"
        raise
        
    line_count = 0

    for i in code:
        i = i.strip()
        if len(i) == 0:
            pass
        elif i[0] == "#":
            pass
        else:
            line_count += 1

    return line_count

if __name__ == "__main__":
    main()
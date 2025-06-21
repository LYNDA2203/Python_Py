import sys
import math

def main():
    if len(sys.argv) != 3:
        print("Please provide exactly two integer arguments:X and Y")
        return
    
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    
    distance = math.sqrt(math.pow(x,2)+ math.pow(y,2))
    
    print(f"Distance from ({x},{y}) to (0,0) is: {distance}")
    
if __name__ == "__main__":
    main()
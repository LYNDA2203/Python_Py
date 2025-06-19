# Number=int(input("Enter the number:"))
# hormonic=0.0
# if Number > 0:
#     for i in range(1,Number+1):
#         hormonic += 1/i
#     print(f"The {Number}th Harmonic Value is:{hormonic:.4f}")
# else:
#     print("please enter the value greater than 0")



#if its in command_line
import sys

if len(sys.argv) != 2:
    print("Enter with atleast one argument (eg.. py file_name.py <N>)")
else:
    N=int(sys.argv[1])
    if N < 0:
        print("Please enter the value more than 0")
    else:
        hormonic = 0.0
        for i in range(1,N+1):
             hormonic += 1/i
        print(f"The {N}th Harmonic Value is:{hormonic:.4f}")
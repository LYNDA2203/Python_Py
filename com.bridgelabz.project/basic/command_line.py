import sys
if (len(sys.argv) != 2):
     print("please enter atleast one argument(eg. py file_name.py <N>)")
else:
    N = int(sys.argv[1])
    
    if 0 <= N <= 31:
        print(f"Enter the value of 2 to the power of {N}")
        for i in range(N+1):
            print(f"2^{i} = {2**i}")
    else:
            print(f"Please enter the values between 0 to 31")
            
num =int(input("Enter the number:"))

if num <= 1:
    print("Please enter the value more than 1")
else:
    print(f"The Prime factors of {num} is:", end=' ')
    i = 2
    while i*i <= num:
        while num % i == 0:
            print(i, end=' ')
            num=num//i
        i += 1
    if num > 1:
        print(num)
    else:
        print()
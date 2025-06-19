import random

number=int(input("Enter the number of flips:"))
head = 0
tail = 0
if number < 0:
    print("please enter the positive integer....")
else:
    for _  in range(number):
        if random.random() < 0.5:
            tail += 1
        else:
            head +=1
head_percent= (head/number)*100
tail_percent= (tail/number)*100
        
print(f"TOtal number of flips:{number}")
print(f"Head:{head} ({head_percent:.2f}%)")
print(f"Tail: {tail} ({tail_percent:.2f}%)")

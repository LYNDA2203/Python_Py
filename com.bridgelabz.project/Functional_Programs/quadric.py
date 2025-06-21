import math

a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))

delta=b*b-4*a*c

if delta > 0:
    root1=(-b + math.sqrt(delta))/(2*a)
    root2=(-b - math.sqrt(delta))/(2*a)
    
    print("Two real and  distinct roots are....")
    print(f"The value of Root 1:",root1)
    print(f"The value of Root 2:",root2)
elif delta == 0:
    root=-b/(2*a)
    
    #printing the values of roots
    print("Two real and equal roots are.....")
    print(f"the value of Root1:",root)

else:
    real_part=-b/(2*a)
    img_part= math.sqrt(-delta)/(2*a)
    
    #printing the values of real and imaginary part of roots
    print("Two Complex roots..")
    print("Root1: {} + {}i".format(real_part,img_part))
    print("Root2: {} - {}i".format(real_part,img_part))
    
import random
x= random.randint(1,20)
y= random.randint(1,10)
print(f"{x} * {y} = ?")

try:
    user_input = int(input("Your answer: "))
    if user_input == (x*y):
        print("You are correct")
    else:
        print("Correct answer : {x*y}")
except ValueError:
    print("Please insert an integer")

import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1,100))

print(numbers)
def apply_operation(numbers, operation):

    if operation == 1:
        multiplyby3 = list(map(lambda x: x * 3, numbers))
        print(f"{numbers} multiplied by 3 : {multiplyby3}")
    elif operation == 2:
        multiplesof4 = list(filter(lambda x: x % 4 == 0, numbers))
        if multiplesof4 == []:
            print(f"There are no multipples of 4 in {numbers}")
        else:
            print(f"Multiples of 4 in {numbers} : {multiplesof4}")
    elif operation == 3:
        descendingorder = list(sorted(numbers, reverse=True))
        print(f"{numbers} in descending order: {descendingorder}")
    elif operation == 4:
        ascendingorder = list(sorted(numbers))
        print(f"{numbers} in ascending order: {ascendingorder}")
    elif operation == 5:
        total = sum(numbers)
        print(f"Sum of the elements in {numbers} is {total}")




try:
    user_input = int(input("Please choose the number referring to the operation that you want to use on a randomly generated list of 10 integers:\n"
      "1. Multiply all the list elements by 3\n"
      "2. Find the multiples of 4\n"
      "3. Sort by descending order\n"
      "4. Sort by ascending order\n"
      "5. Calculate the sum of all numbers\n"      
      "Which operation would you like to perform? "
                           ))
    apply_operation(numbers, user_input)
except ValueError:
    print("Please insert an integer")




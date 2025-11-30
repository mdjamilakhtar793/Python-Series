input_str = "teeteracdacd"

for char in input_str:
    print(char)
    if input_str.count(char) == 1:
        print("Char is: ", char)
        break
number = 5
factorial = 1

while number > 0:
    # factorial = factorial * number
    # number = number - 1
    factorial *= number
    number -= 1

print("Factorial: ", factorial)
while True:
    number = int(input("Enter value b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, try again")


number = 28

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break

print(is_prime)


items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate: ", item)
        break
    unique_item.add(item)

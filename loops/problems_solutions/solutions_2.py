n = 10
sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1

print("Sum of even number is: , ", sum_even)


number = 3

for i in range(1, 11):
    if i == 5:
        continue
    print(number, 'x', i, '=', number * i)

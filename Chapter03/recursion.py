# getting factorial using for loop
fact = 1
num = 3
for index in range(1, num + 1):
    fact = fact * index

print(fact)


def factorial(number):
    if number < 0:
        return

    if number == 1 or number == 0:
        return 1

    return number * factorial(number - 1)


print(factorial(3))

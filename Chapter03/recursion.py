# getting factorial using for loop
fact = 1
num = 3
for index in range(1, num + 1):
    fact = fact * index


# factorial depends on stack
def factorial(number):
    if number < 0:
        return

    if number == 1 or number == 0:
        return 1

    return number * factorial(number - 1)


# Enhance factorial using dictionary as cash
factorial_cash = {}


# a function getting factorial from cash dictionary if exists otherwise it depends on factorial recursion function
def get_number_factorial(number, factorial_dictionary):
    if number in factorial_dictionary.keys():
        number_factorial = factorial_dictionary[number]
        return number_factorial
    else:
        number_factorial = factorial(number)
        factorial_dictionary[number] = number_factorial
        return factorial(number)


print(get_number_factorial(3, factorial_cash))
print(get_number_factorial(3, factorial_cash))

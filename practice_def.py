# Plus
def plus(d, c: int = 0):
    total = c + d
    return total


def get_numbers():
    print("Plus")
    a = int(input('Enter first digit: '))
    b = int(input('Enter second digit: '))
    return a, b


# total = plus()
# print(total)  # print(plus())

# print(plus(c=a, d=b))
# plus()

# a, b = get_numbers()
# total = plus(d=b, c=a)
# print(total)





# Minus
def minus(c, d: int = 0):
    result = c - d
    return result


def get_minus_num():
    print("Minus")
    a = int(input('Enter first digit: '))
    b = int(input('Enter second digit: '))
    return a, b

# a, b = get_date()
# result = minus(c=a, d=b)
# print(result)


#  Multiplication

def multiplication(c, d):
    answer = c * d
    return answer


def get_multiplication_num():
    print("Multiplication")
    first_multiplication = int(input('Enter first digit: '))
    second_multiplication = int(input('Enter second digit: '))
    return first_multiplication, second_multiplication

# a, b = get_multiplication_num()
# result = multiplication(c=a, d=b)
# print(result)

def division(c, d):
    result = c / d
    return result


def get_division_num():
    print("Division")
    first_division = int(input('Enter first digit: '))
    second_division = int(input('Enter second digit: '))
    return first_division, second_division


print(f"Your answer --> {plus(*get_numbers())}")
print(f"Your answer --> {minus(*get_minus_num())}")
print(f"Your answer --> {multiplication(*get_multiplication_num())}")
print(f"Your answer --> {division(*get_division_num())}")
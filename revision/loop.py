numbers = [1, 23, 45, 67, 89, 12, 34, 56, 78, 90]


def check_number(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"


for number in numbers:
   print(check_number(number))

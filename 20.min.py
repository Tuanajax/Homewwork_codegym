
from re import A


def get_min_numbers(numbers):
    result = int(numbers[0])
    for num in numbers:
        if int(result) > int(num):
            result = num
    return  result
numbers = input("Enter numbers:")
min_number = get_min_numbers(numbers)
print("Min number: ", min_number)
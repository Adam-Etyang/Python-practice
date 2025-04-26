def sum_of_digits(number):
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    return total


if __name__ == "__main__":
    while True:
        print("press ctrl + c to exit")
        number = int(input("enter a number: "))
        print(f"the sum of the digits in the number{number} is {sum_of_digits(number)}")

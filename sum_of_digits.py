def sum_of_digits(number):
    total = 0
    while number > 0:  # the loop will run until number has been reduced to 0
        digit = number % 10  # getting the last digit from the number
        total += digit  # adding the last digit to the total
        number = number // 10  # removing the last digit from number
    return total


if __name__ == "__main__":
    while True:
        print("press ctrl + c to exit")
        number = int(input("enter a number: "))
        print(f"the sum of the digits in the number{number} is {sum_of_digits(number)}")

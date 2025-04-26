def factorial(num):
    if num == 0:  # base case
        return 1
    else:  # recursive case
        return num * factorial(num - 1)


if __name__ == "__main__":
    num = int(input("enter a number: "))
    print(f"{num} factorial is {factorial(num)}")

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact


if __name__ == "__main__":
    num = int(input("enter a number: "))
    print(f"{num} factorial is {factorial(num)}")

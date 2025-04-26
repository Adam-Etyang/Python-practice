def even_or_odd(num):
    if num % 2 == 0:
        print("the number is even")
    else:
        print("the number is odd")


if __name__ == "__main__":
    number = int(input("enter a number: "))
    even_or_odd(number)

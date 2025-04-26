# function to check if a number is even or odd
def even_or_odd(num):
    if num % 2 == 0:  # uses the mod operator to check if the number is even
        print("the number is even")
    else:
        print("the number is odd")


if __name__ == "__main__":
    number = int(input("enter a number: "))  # getting input from the user
    even_or_odd(number)

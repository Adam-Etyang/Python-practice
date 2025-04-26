def reversed(string):
    reversed = ""
    for i in string:
        reversed = i + reversed
    return reversed


if __name__ == "__main__":
    while True:
        print("press ctrl + c to exit")
        string = str(input("enter a word: "))
        print(f"{string} reversed is {reversed(string)}")

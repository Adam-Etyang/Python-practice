def sum_of_list(elements):
    num = 0
    for i in elements:
        num += i
    return num


if "__main__" == __name__:
    input_list = []
    while True:
        elements = input(
            "enter the elements of the list (types 'done' or 'stop' when finished)"
        )
        if elements == "done" or elements == "stop":
            break
        try:
            numbers = float(elements)
            input_list.append(numbers)
        except ValueError:
            print("please enter a valid number")
    print(f"your list is :{input_list}\n")
    print(f"the sum of elements in your list is:{sum(input_list)}")

import time


# function that uses iteration to find the sum of elements in a list
def sum_iterative(elements):
    num = 0
    for i in elements:
        num += i
    return num


# recursive version of the function above to find the sum of elements in a list
def sum_recursive(elements):
    if len(elements) == 0:
        return 0
    else:
        return elements[0] + sum_recursive(elements[1:])


# getting user input to add elements into a list and call the above funtions to find the sum and compare the speeds of the two different approaches
if __name__ == "__main__":
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
    # timing iterative function:
    start_iterative = time.time()
    iterative_sum = sum_iterative(input_list)
    end_interative = time.time()
    iterative_time = end_interative - start_iterative

    # timing recursive function
    start_recursive = time.time()
    recursive_sum = sum_recursive(input_list)
    end_recursive = time.time()
    recursive_time = end_recursive - start_recursive

    # output of the results
    print(f"your list is :{input_list}\n")
    print(
        f"the sum of elements using iteration is :{iterative_sum} and it took {iterative_time:.6f}seconds"
    )
    print(
        f"the sum of elements of the list using recursion is :{recursive_sum} and it took {recursive_time:.6f} seconds"
    )

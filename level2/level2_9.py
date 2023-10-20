def perform_operation_on_list(my_list, index):
    try:
        result = my_list[index]  # Perform the desired operation
        return result
    except IndexError:
        return "Index is out of range"
my_list = [1, 2, 3, 4, 5]
index = 2
try:
    output = perform_operation_on_list(my_list, index)
    print("Result:", output)
except IndexError as e:
    print(f"Exception: {e}")

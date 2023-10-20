def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
list1 = [1, 2, 2, 3, 4, 4, 5, 5]
list2 = unique_elements(list1)
print("Unique elements:", list2)

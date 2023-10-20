input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
frequency_count = {}
for element in input_list:
    if element in frequency_count:
        frequency_count[element] += 1
    else:
        frequency_count[element] = 1
print("Frequency count:", frequency_count)

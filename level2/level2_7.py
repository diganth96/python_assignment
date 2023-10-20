def find_median(number_list):
    sorted_list = sorted(number_list)
    n = len(sorted_list)

    if n % 2 == 1:
        median = sorted_list[n // 2]
    else:
        middle1 = sorted_list[n // 2 - 1]
        middle2 = sorted_list[n // 2]
        median = (middle1 + middle2) / 2

    return median
number_list = [7, 2, 5, 1, 9, 3]
median = find_median(number_list)
print("Median:", median)

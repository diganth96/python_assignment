def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    arr[:n-d] = arr[:n-d][::-1]
    arr[n-d:] = arr[n-d:][::-1]
    arr[:] = arr[::-1]
arr = [1, 2, 3, 4, 5]
D = 2
rotate_array(arr, D)
print("arr after rotation =", arr)
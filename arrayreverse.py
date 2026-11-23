arr = [6, 5, 4, 3, 2, 1]
arr_size = len(arr)
print("Original array:", arr)

for i in range(arr_size // 2):
    opposite_index = arr_size - 1 - i

    temp = arr[i]
    arr[i] = arr[opposite_index]
    arr[opposite_index] = temp

print("Reversed array:", arr)

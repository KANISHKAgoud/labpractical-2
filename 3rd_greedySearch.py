def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current i is the index of the minimum value
        min_index = i

        # Find the actual minimum element in the rest of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the current i-th element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

numbers = [64, 25, 12, 22, 11]
sorted_numbers = selection_sort(numbers)

print("Sorted list:", sorted_numbers)

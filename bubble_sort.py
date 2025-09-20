def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = [55, 32, 27, 18, 15, 46, 81]
bubble_sort(arr)
print('Sorted array:', arr)

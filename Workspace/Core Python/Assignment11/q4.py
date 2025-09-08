# Ascending bubble sort, then take second from end
arr = [12, 7, 19, 3, 19, 8]

n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Second largest (not necessarily distinct)
second_largest = arr[-2] if n >= 2 else None
print("Second largest:", second_largest)

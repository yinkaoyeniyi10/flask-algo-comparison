def bubble_sort(data):
    arr = data.copy()
    comps, swaps = 0, 0
    n = len(arr)
    #Traverse through all variables
    for i in range(n):
        for j in range(0, n - i - 1):
            comps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
            yield arr.copy(), comps, swaps, (j, j+1)
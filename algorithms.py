def bubble_sort(data):
    #Makes a copy so original list isn't modified
    arr = data.copy()
    #Keeps track of performance
    comps, swaps = 0, 0
    n = len(arr)
    #Traverse through all variables
    for i in range(n):
        #Compares adjacent elements
        for j in range(0, n - i - 1):
            comps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
            #return the current state for the visualizer. this includes the list, comp #, swap #, and current indices
            yield arr.copy(), comps, swaps, (j, j+1)
ALGORITHMS = {
    "Bubble Sort": bubble_sort
}
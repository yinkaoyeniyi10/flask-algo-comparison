# Yinka Oyeniyi, Juveriyah Haq
def bubble_sort(data):
    #Makes a copy so original list isn't modified
    arr = data.copy()
    #Keeps track of performance
    comps, swaps = 0, 0
    n = len(arr)
    #Traverse through all variables
    for i in range(n):
        swapped=False
        #Compares adjacent elements
        for j in range(0, n - i - 1):
            comps += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped=True
                swaps += 1
            #return the current state for the visualizer. this includes the list, comp #, swap #, and current indices
            yield arr.copy(), comps, swaps, (j, j+1)
        #If no swaps are made, it must be sorted...
        if not swapped:
            break
    yield arr.copy(), comps, swaps, ()

def insertion_sort(data):
    arr =  data.copy()
    comps, swaps = 0, 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comps += 1
            yield arr.copy(), comps, swaps, (j, j + 1)
            if arr[j] > key:
                arr[j +1] = arr[j]
                swaps += 1
                yield arr.copy(), comps, swaps, (j, j+1)
                j -= 1
            else:
                break
        arr[j + 1] = key
    yield arr.copy(), comps, swaps, ()

def selection_sort(data):
    arr = data.copy()
    comps, swaps = 0, 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comps += 1
            yield arr.copy(), comps, swaps, (min_idx, j)
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            yield arr.copy(), comps, swaps, (i, min_idx)
    yield arr.copy(), comps, swaps, ()
            

ALGORITHMS = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
}

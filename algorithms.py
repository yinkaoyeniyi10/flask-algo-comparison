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
    yeild arr.copy(), comps, swaps, ()

def insertion_sort(data):
    arr =  data.copy()
    comps, swaps = 0, 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comps += 1
            yeild arr.copy(), comps, swaps, (j, j + 1)
            if arr[j] > key:
                arr[j +1] = arr[j]
                swaps += 1
                yeild arr.copy(), comps, swaps, (j, j+1)
                 j -= 1
            else:
                break
        arr[j + 1] = key
    yeild arr.copy(), comps, swaps()
            
           


ALGORITHMS = {
    "Bubble Sort": bubble_sort
}

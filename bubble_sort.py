def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[i], arr[j+1] = arr[j+1], arr[i]
    print(arr) 

bubble_sort([23,12,30,10,4,57])               

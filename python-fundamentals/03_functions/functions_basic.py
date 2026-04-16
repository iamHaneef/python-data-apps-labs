unsorted1 = [23, 1, 56, 33, 99, 10]
unsorted2 = [23, 1, 56, 33, 99, 10]


def asc_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


def desc_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


print("The Ascending Sorted Array is : ", asc_sort(unsorted1))
print("The Descending Sorted Array is : ", desc_sort(unsorted2))

# prebuild method for Sorting

arr1 = [23, 1, 56, 33, 99, 10]
arr2 = [23, 1, 56, 33, 99, 10]

print("The Ascending Sorted Array is : ", sorted(arr1))
(print("The Descending Sorted Array is : ", sorted(arr2, reverse=True)))

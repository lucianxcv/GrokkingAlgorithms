def find_smallest(arr):
    smallest = arr[0]      # Store the smallest value
    smallest_index = 0     # Store the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr

print(selection_sort([5, 3, 6, 2, 10]))


"""
The code starts by looking through a list of numbers to find the smallest one.

It keeps track of which number is the smallest, and also remembers where it is in the list.

Once it finds the smallest number, it removes it from the list and adds it to a new list.

Then it goes back to the remaining numbers and finds the next smallest one.

It repeats this process: find the smallest, remove it, and add it to the new list.

This keeps going until the original list is empty.

By the end, the new list contains all the numbers in order from smallest to biggest.

The original list is now empty, and the new list is the sorted version."""
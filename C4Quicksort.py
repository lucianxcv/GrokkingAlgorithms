def quicksort(array):
    if len(array) < 2:
        return array  # Base case: arrays with 0 or 1 element are already sorted
    else:
        pivot = array[0]  # Recursive case
        less = [i for i in array[1:] if i <= pivot]  # Elements less than or equal to pivot
        greater = [i for i in array[1:] if i > pivot]  # Elements greater than pivot
        return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([10, 5, 2, 3]))

"""What is Quicksort doing?
It sorts a list by:

Picking one number as a “pivot”

Splitting the rest into two groups:

Numbers less than or equal to the pivot

Numbers greater than the pivot

Then it repeats this same process on both groups, separately.

Base Case
If the list has 0 or 1 items, it’s already sorted. No need to do anything — just return it as-is.

Recursive Case
For longer lists:

Pick the first number as the pivot

Put all smaller numbers in one list (less)

Put all bigger numbers in another list (greater)

Sort each of those smaller lists by calling the function again

Put the final list together as:

Sorted less part → the pivot → sorted greater part

quicksort([10, 5, 2, 3])
Pivot = 10

less = [5, 2, 3]
greater = []

Recursively quicksort [5, 2, 3]

Pivot = 5

less = [2, 3]

greater = []

Recursively quicksort [2, 3]

Pivot = 2

less = []

greater = [3]

Result = [2, 3]

Result = [2, 3, 5]

Final result = [2, 3, 5, 10]"""

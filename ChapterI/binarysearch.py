my_list = [1, 3, 5, 7, 9]

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == item:
            return mid  # Found the item
        if guess > item:
            high = mid - 1  # Guess was too high
        else:
            low = mid + 1  # Guess was too low

    return None  # Item doesn't exist

print(binary_search(my_list, 9))
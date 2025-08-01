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

"""You start with a sorted list of numbers (from smallest to biggest).

You’re looking for a specific number in that list.

Instead of checking every number one by one, the code starts by checking the middle number.

If the middle number is exactly the one you're looking for, it returns the position — done!

If the number you're looking for is smaller than the middle number, the code knows the answer must be in the left half of the list — so it ignores the right half completely.

If the number you're looking for is bigger than the middle number, the code knows it must be in the right half — so it ignores the left half.

Then it repeats the process with the remaining half:

Check the new middle number,

Compare it to the one you’re looking for,

Keep cutting the list in half.

This continues until either:

It finds your number and tells you where it is,

Or it runs out of numbers to check (meaning the number isn’t in the list at all).

Think of it like guessing a number between 1 and 100:

You start by guessing 50.

If it’s too high, you guess halfway between 1 and 50.

If it’s too low, you guess halfway between 50 and 100.

You narrow it down quickly — that's binary search.

It’s much faster than checking each number one by one — especially with long lists."""
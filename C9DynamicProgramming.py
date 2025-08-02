def knapsack(items, max_weight):
    # Create a 2D array with rows = items and cols = max weight + 1
    table = [[0 for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        name, value, weight = items[i - 1]
        for w in range(1, max_weight + 1):
            if weight > w:
                table[i][w] = table[i - 1][w]
            else:
                table[i][w] = max(table[i - 1][w], table[i - 1][w - weight] + value)

    return table[-1][-1]


items = [
    ("guitar", 1500, 1),
    ("stereo", 3000, 4),
    ("laptop", 2000, 3)
]

max_weight = 4
print(knapsack(items, max_weight))  # Output: 3500

"""
table = [[0 ...]]
A 2D list: rows = items + 1, columns = weight limits from 0 to max.

Each cell will store the maximum value that can be carried with that number of items and that weight.

Loop through items:
python
Copy
Edit
for i in range(1, len(items) + 1):
We start at 1 because row 0 is the base case (no items = 0 value).

Get item info:
python
Copy
Edit
name, value, weight = items[i - 1]
We subtract 1 from i since table starts from 1 but items list is 0-indexed.

Loop through weights:
python
Copy
Edit
for w in range(1, max_weight + 1):
For each possible knapsack weight from 1 to max.

If item doesn’t fit:
python
Copy
Edit
if weight > w:
    table[i][w] = table[i - 1][w]
Copy the value from the row above — item can’t be included.

If item fits:
python
Copy
Edit
else:
    table[i][w] = max(
        table[i - 1][w],  # Don’t include item
        table[i - 1][w - weight] + value  # Include item
    )
Choose the better of two options:

Skip the item

Include it and add its value to the best value for remaining weight

Return the answer:
python
Copy
Edit
return table[-1][-1]
Bottom-right cell contains the max value possible.

🔍 VISUAL IDEA:
Imagine a spreadsheet:

Rows = each item

Columns = increasing weight capacity

Fill it step-by-step to build up to the optimal answer

✅ Big Idea of Dynamic Programming
Break problem into smaller subproblems

Store results of subproblems to avoid duplicate work (this is the “dynamic” part)

Build up to the full solution using a table (bottom-up
"""
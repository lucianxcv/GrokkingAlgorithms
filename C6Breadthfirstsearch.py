from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'  # Example condition: names ending in 'm' are sellers

def search(name):
    search_queue = deque()
    search_queue += graph[name]  # Start with the person's immediate neighbors
    searched = []  # Keep track of people already searched

    while search_queue:
        person = search_queue.popleft()  # Get the next person from the queue
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} is a mango seller!")
                return True
            else:
                search_queue += graph[person]  # Add this person's neighbors to the queue
                searched.append(person)
    return False

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search("you")

"""
from collections import deque
Purpose: Imports the deque (double-ended queue) class.

Why: deque is faster than a regular list when you're constantly adding/removing items from the beginning of the list.

def person_is_seller(name):
Purpose: Defines a helper function that checks if a person is a mango seller.

return name[-1] == 'm'
Purpose: Returns True if the person’s name ends with 'm' (e.g., "thom").

Why: This is just a placeholder condition to simulate a seller-check. You can change this logic based on your real-world scenario.

def search(name):
Purpose: Defines the main BFS function.

Input: Takes a starting person's name (like "you").

search_queue = deque()
Purpose: Initializes an empty queue to keep track of who to search next.

search_queue += graph[name]
Purpose: Adds the immediate neighbors (friends) of the starting person to the queue.

searched = []
Purpose: Creates a list to track people you’ve already checked.

Why: Prevents looping over the same people multiple times (avoids infinite loops).

while search_queue:
Purpose: Loops as long as there are people in the queue.

Meaning: “While there’s someone we haven’t checked…”

person = search_queue.popleft()
Purpose: Gets the first person from the queue to check.

Why: popleft() efficiently removes and returns the leftmost item.

if person not in searched:
Purpose: Checks if we’ve already looked at this person before.

if person_is_seller(person):
Purpose: Calls the earlier function to check if this person sells mangoes.

print(f"{person} is a mango seller!")
Purpose: If they are a seller, prints a success message.

return True
Purpose: Ends the function and returns True — we found the seller!

else:
Purpose: If the person isn’t a seller…

search_queue += graph[person]
Purpose: Add this person’s friends/neighbors to the queue to check them next.

searched.append(person)
Purpose: Marks this person as already checked.

return False
Purpose: If the whole queue is exhausted and no seller is found, return False.

"""
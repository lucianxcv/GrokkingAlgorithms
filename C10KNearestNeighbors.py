"""
Smmary of Chapter 10 – K-Nearest Neighbors (k-NN)
k-NN is an algorithm that:

Stores all the training data (it doesn’t “learn” in the traditional sense).

When asked to make a prediction (like “Is this fruit an apple or orange?”), it:

Looks at the k closest data points (neighbors) in the training set.

Chooses the majority class from those neighbors.

It's mainly used for:

Classification (e.g., spam or not spam)

Recommendation systems (e.g., similar users)

Simple predictions based on proximity

💡 Key Concepts
Distance: k-NN needs a way to measure how “close” two data points are. It usually uses Euclidean distance for that (like the straight-line distance on a graph).

k: The number of neighbors it considers. Choosing the right k is important:

If k is too low (like 1), predictions may be too sensitive to noise.

If k is too high, it might average too many irrelevant neighbors
"""
from math import sqrt

# Sample dataset: (sweetness, crunchiness)
dataset = {
    "Alice":    [1.0, 1.0],   # didn't like
    "Bob":      [2.0, 1.5],   # didn't like
    "Charlie":  [3.0, 3.5],   # liked
    "Diana":    [3.5, 4.0],   # liked
}

# Their preferences (label)
labels = {
    "Alice": "no",
    "Bob": "no",
    "Charlie": "yes",
    "Diana": "yes",
}

# Function to compute Euclidean distance
def euclidean_distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# k-NN function
def knn(data, labels, query, k=3):
    distances = []

    for person in data:
        dist = euclidean_distance(data[person], query)
        distances.append((dist, labels[person]))

    # Sort by distance
    distances.sort()
    # Take the k nearest labels
    k_nearest = distances[:k]

    # Count the votes
    results = {"yes": 0, "no": 0}
    for _, label in k_nearest:
        results[label] += 1

    # Return the majority vote
    return "yes" if results["yes"] > results["no"] else "no"

# Test: predict if someone likes the fruit with sweetness=3.0 and crunchiness=3.0
print(knn(dataset, labels, [3.0, 3.0], k=3))  # Output: "yes"


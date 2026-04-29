# Level 1 - The Essential Patterns (Core Lego Bricks)

# Linear Search - small or unsorted lists
for item in items:
    if item == target:
        return True
    return False

# Binary Search - large sorted lists
def binary_search(items, target):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = items[mid]

        if guess == target:
            return True
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return False

# Selection Sort - small lists
def selection_sort(items):
    for i in range(len(items)):
        min_index = i
        for j in range (i + 1, len(items)):
            if items[j] < items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]

# Bubble Sort - small lists, educational purposes
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

# Filter - select items that meet a condition
matches = [x for x in items if condition(x)]

# max()/min() - find the largest/smallest item
winner = max(items, key=lambda x: x.score)

# Map/Reduce - apply function to items and combine results
from functools import reduce
squared = [x**2 for x in items]
total = sum(items)

# Duplicate Detection - using a set
# fastest way to detect duplicates in a set
seen = set()
for x in items:
    if x in seen:
        return True
    seen.add(x)
    return False

# Count with dictionary - when you need frequency counts
counts = {}
for x in items:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

# Count with Counter - simpler and more efficient
from collections import Counter
counts = Counter(items)

# Zip combine two lists into a list of tuples
combined = list(zip(list1, list2))

# unzip a list of tuples into two lists
list1, list2 = zip(*combined)

# Looping Patterns - How do I walk through data?
# Enumerate - loop with index and value
for index, value in enumerate(items):
    print(f"Index: {index}, Value: {value}")

# Looping with multiple lists
for a, b in zip(list1, list2):
    print(f"A: {a}, B: {b}")

# Early Exit - break out of loops when done
for item in items:
    if condition(item):
        break

# Problem-Solving Patterns - How do I structure logic?
# If-Else - Basic decision making
if condition1:
    do_something()
elif condition2:
    do_something_else()
else:
    do_default()
    
# Best-So-Far
best = None
for x in items:
    if best is None or x > best:
        best = x

# Two Pointers - when you need to compare or combine two sequences
left, right = 0, len(items) - 1
while left < right:
    if condition(items[left], items[right]):
        do_something()
        left += 1
    else:
        right -= 1

# Sliding Window - When you need to find a contiguous subarray that meets a condition
window_sum = 0
left = 0
for right in range(len(nums)):
    window_sum += nums[right]
    while window_sum > target:
        window_sum -= nums[left]
        left += 1
    if window_sum == target:
        return True
    
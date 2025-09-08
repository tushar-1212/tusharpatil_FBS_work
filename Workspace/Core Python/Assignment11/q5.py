words = ["apple", "kiwi", "banana", "fig", "grape"]

# Bubble sort based on length
n = len(words)
for i in range(n):
    for j in range(0, n-i-1):
        if len(words[j]) > len(words[j+1]):
            words[j], words[j+1] = words[j+1], words[j]

print("Sorted list by length:", words)

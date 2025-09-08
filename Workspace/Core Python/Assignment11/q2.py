# Function to merge and sort two lists
def merge_and_sort(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

list1 = []
list2 = []

c1 = int(input("Enter number of elements for List 1: "))
for i in range(c1):
    list1 += [int(input(f"Enter element {i+1} for List 1: "))]

c2 = int(input("Enter number of elements for List 2: "))
for i in range(c2):
    list2 += [int(input(f"Enter element {i+1} for List 2: "))]


result = merge_and_sort(list1, list2)
print("Merged and Sorted List:", result)

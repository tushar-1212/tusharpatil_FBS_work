

def list_to_dict(lst):
    freq = {}
    for num in lst:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq


list1 = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]

dict = list_to_dict(list1)

print(dict)



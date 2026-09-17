# 1. Frequency Counting (using a Dictionary)
items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
freq_dict = {}
for item in items:
    if item in freq_dict:
        freq_dict[item] += 1
    else:
        freq_dict[item] = 1
print("1. Frequency Count:", freq_dict)

# 2. Sorting (Dictionary)
# Sorting the dictionary by its keys
sorted_dict = dict(sorted(freq_dict.items()))
print("2. Sorted Dictionary (by keys):", sorted_dict)

# 3. Merging (Dictionaries)
dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}
merged_dict = dict1.copy()
merged_dict.update(dict2)
print("3. Merged Dictionary:", merged_dict)

# 4. Common and Unique Elements (using Sets)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Identifying common elements (Intersection)
common_elements = set1.intersection(set2)
print("4. Common Elements (Intersection):", common_elements)

# Identifying unique elements to set1 (Difference)
unique_to_set1 = set1.difference(set2)
print("5. Unique to Set 1 (Difference):", unique_to_set1)

# Identifying elements unique to both (Symmetric Difference)
unique_all = set1.symmetric_difference(set2)
print("6. Unique to both sets (Symmetric Difference):", unique_all)
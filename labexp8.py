initial_list = input("Enter sequence of comma-separated numbers: ")

converted_list = initial_list.split(",")

number_list = []
for i in converted_list:
    cleaned = i.strip()
    number_list.append(cleaned)

number_tuple = tuple(number_list)

print("List: ", number_list)
print("Tuple: ", number_tuple)

total = len(number_list)
print("Total number of elements: ", total)

print("First Element: ", number_list[0])
print("Last Element: ", number_list[-1])

print("Reversed List: ", number_list[::-1])
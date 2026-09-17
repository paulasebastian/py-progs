marks = [45, 82, 15, 67, 91, 34]
print("Original List:", marks)

marks.append(50)
marks.insert(2, 75)
marks.remove(15)
marks.sort()
print("After Manipulation (Appended, Inserted, Removed, Sorted):", marks)

search_value = 67
if search_value in marks:
    index = marks.index(search_value)
    print(f"Search: {search_value} is found at index {index}")

marks[0] = 40
print("After Update (Changed index 0 to 40):", marks)

high_marks = [mark for mark in marks if mark > 60]
print("Filtered List (Marks > 60):", high_marks)
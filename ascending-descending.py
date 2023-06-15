
list1 = []

num_elements = int(input("Enter the number of elements: "))
for i in range(num_elements):
    element = int(input("Enter element {}: ".format(i + 1)))
    list1.append(element)

for i in range(len(list1) - 1):
    for j in range(0, len(list1) - i - 1):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]

sorted_list = []
reverse_sort = []
for element in list1:
    sorted_list.append(element)
for i in range(num_elements - 1, -1, -1):
    reverse_sort.append(sorted_list[i])

print("The sorted list is: ", sorted_list)
print("Descending order : ", reverse_sort)

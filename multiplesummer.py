# Give the sum of all multiples of 3 and 5 under 5000


new_list = []
list_creator = 0
while list_creator < 4999:
    list_creator = list_creator + 1
    new_list.append(list_creator)
total = 0
for i in new_list:
    if i % 3 == 0 or i % 5 == 0:
        total = total + i
        continue
print(total)

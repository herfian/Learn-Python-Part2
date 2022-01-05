# Find Duplicates

my_list = ['a','a','b','c','b','d','e','f','e']

duplicates = []

for value in my_list:
  if my_list.count(value) > 1:
    if value not in duplicates:
      duplicates.append(value)

print(duplicates)

# Output :
# ['a', 'b', 'e']
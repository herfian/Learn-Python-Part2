for i,char in enumerate([1,2,3,4,5]):
  print(i, char)

# Output :
# 0 1
# 1 2
# 2 3
# 3 4
# 4 5

for i,char in enumerate(list(range(100))):
  print(i, char)
  if char == 50:
    print(f'index of 50 is : {i}')
    # Output : index of 50 is : 50
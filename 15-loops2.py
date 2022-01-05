my_list = [1,2,3,4,5]

for item in my_list:
  print(item) 
  break
  # Output : 1

i = 0
while i < len(my_list):
  print(my_list[i])
  i += 1
  continue
# Output :
# 1
# 2
# 3
# 4
# 5

for item in my_list:
  # print(item) 
  pass
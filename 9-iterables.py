# Iterables = list, dictionary, tuple, set, string
# Iterate = one by one check each item in the collection (Iterables)

user = {
  'Name' : 'Golem',
  'Age' : 1000,
  'Can_Swim' : False
}

for item in user: # item = Iterate
  print(item) # user = Iterables

# Output :
# Name
# Age
# Can_Swim

for item in user.items(): # Method()
  print(item)

# Output :
# ('Name', 'Golem')
# ('Age', 1000)
# ('Can_Swim', False)

for item in user.values():
  print(item)

# Output :
# Golem
# 1000
# False

for item in user.keys():
  print(item)

# Output :
# Name
# Age
# Can_Swim

for key, value in user.items():
  print(key, value)

# Output :
# Name Golem
# Age 1000
# Can_Swim False
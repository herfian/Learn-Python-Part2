# is vs ==
print(True == 1) # True
print('' == 1) # False
print([] == 1) # False
print(10 == 10.0) # True
print([] == []) # True

# is
print(True is 1) # False
print(True is True) # True
print('' is 1) # False
print(1 is 1) # True
print([] is 1) # False
print(10 is 10.0) # False
print([] is []) # False
a = [1,2,3]
b = [1,2,3]
print(a is b) # False
print(a == b) # True
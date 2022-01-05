# Truthy vs Falsey
username = 'Zack'
password = 12345

# Output :
print(bool('Zack')) # True
print(bool(12345)) # True
print(bool('')) # False
print(bool(0)) # False

if username and password:
  print('Login')
else:
  print('Wrong')

# Output :  Login
import random

letters="abcsefghijklmnopqrstuvwxyz"
number="12345676890"
special = "!@#$%^&*()"
chars = letters + number+special

print("Your Password: ")
passw= ""
for x in range(16):
    passw+= random.choice(chars)
print(passw)

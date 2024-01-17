import random
import string

numbers = string.digits

symbols = string.punctuation

small_letters = string.ascii_lowercase

capital_letters = string.ascii_uppercase

all_characters =[numbers,symbols,small_letters,capital_letters]

print(numbers)
print(symbols)
print(small_letters)
print(capital_letters)


password = ""

"""
for i in range(2):
    password+=all_characters[0][random.randint(0,9)]
for i in range(2):
    password += all_characters[1][random.randint(0,9)]
for i in range(2):
    password += all_characters[2][random.randint(0,9)]
for i in range(2):
    password += all_characters[3][random.randint(0,9)]
    
"""

for j in range(4):
    for i in range(2):
        password += all_characters[i][random.randint(0,len(all_characters[i])-1)]



print(password)

password=list(password)
random.shuffle(password)

print(password)

new_password=("")
new_password=new_password.join(password)
print(new_password)

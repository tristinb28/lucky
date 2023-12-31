with open("lucky\\mydefaults.ini.txt", "r") as ini_file:
    data = ini_file.read()

characters = 0
numbers = 0

for char in data:
    if char.isalpha():
        characters += 1
    elif char.isdigit():
        numbers += 1

print(f"The number of characters is {characters}")
print(f"The number of digits is {numbers}")

with open("lucky\\counter.txt", "x") as f:
    f.write(f"The number of characters is {characters}, and the number of digits is {numbers}")

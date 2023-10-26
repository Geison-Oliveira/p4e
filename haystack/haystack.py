import re
file_name = input('Enter the file name: ')
handle = open(file_name)
numbers = list()
total = 0.0
for line in handle:
    regex = re.findall('[0-9]+', line)
    if len(regex) == 0:
        continue
    for index in range(len(regex)):
        number = float(regex[index])
        total = total + number
        total = int(total)
        numbers.append(number)
print(total)
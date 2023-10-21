# Write a program that prompts for a file name, then opens that file and reads
# through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# Desired Output
# Average spam confidence: 0.7507185185185187

name = input("Enter file name: ")
file_handle = open(name)
counter = 0.0
total = 0.0
for line in file_handle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    str_indx = line.find('0')
    number = line[str_indx :]
    counter = counter + 1
    number = float(number)
    total = total + number
mean = total / counter
print('Average spam confidence:', mean)
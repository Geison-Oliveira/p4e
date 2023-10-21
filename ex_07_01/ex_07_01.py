raw_file = input('Enter the file name:\n')
try:
    text = open(raw_file, 'r')
except:
    print("Error. Couldn't find the file.")
    exit()
for i in text:
    i = i.rstrip()
    text = i.upper()
    print(text)
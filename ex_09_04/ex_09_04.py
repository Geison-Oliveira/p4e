# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of
# mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent
# the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of
# times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a
# maximum loop to find the most prolific committer. Desired Output:
# cwen@iupui.edu 5

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
email = list()
send = dict()
key_count = None
value_count = None
for line in handle:
    if line.startswith('From: ') is False:
        continue
    words = line.split()
    word = words[1]
    email.append(word)
for index in range(len(email)):
    send[email[index]] = send.get(email[index], 0) + 1
for key, value in send.items():
    if value_count is None or value > value_count:
        key_count = key
        value_count = value
print(key_count, value_count)
f = open("text.txt", "r")
content = f.read()
print(content)


# Read by line

for line in f:
    print(line)

f.close
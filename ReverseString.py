my_string = "Hello World"

output = ""

# with built in reversed method
for c in reversed(my_string):
    output = output + c

print output

# with manual traversal
output = ""
for i in range(len(my_string) - 1, -1, -1):
    output += my_string[i]

print output
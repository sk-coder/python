import math


def Choose(n, k):
    try:
        n = int(n)
    except ValueError:
        return "invalid"

    try:
        k = int(k)
    except ValueError:
        return "invalid"


    if n >= k and k >= 0:
        return math.factorial(n) // math.factorial(k) // math.factorial(n - k)

    return "invalid"

output = Choose(1, -3)

print output


# test 1 - valid case
output = Choose(4,2)
print "Should be Valid:" + str(output)
if output == 6:
    print "Test Worked"
else:
    print "You messed this up"

# test 2 - valid case
output = Choose(8,4)
print "Should be Valid:" + str(output)

# test 3 - invalid case
output = Choose(2, 4)
print "Should be Invalid:" + str(output)

# test 4 - invalid case
output = Choose(4,-2)
print "Should be Invalid:" + str(output)

# test 5 string values
output = Choose("foo", "bar")
print "Should be Invalid:" + str(output)

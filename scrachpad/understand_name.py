"""
During runtime the python interpreter runs your code, and it does two things:

1) it sets a few special variables like __name__, and then
2) it executes all the codes it finds in the file.
"""

print("before import")
import math

print("before function_a")
def function_a():
    print("Function A")


print("before function_b")
def function_b():
    print("Function B {}".format(math.sqrt(100)))


print("before __name__ guard")
if __name__ == '__main__':
    function_a()
    function_b()
print("after __name__ guard")

"""
What happen when you run this code in the context of __name__?

1) The interpreter assigns the hard coded __main__ to __name__
"""
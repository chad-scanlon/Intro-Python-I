"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
f = open('./foo.txt', 'r')
print(f.read())
f.close()
# print(f.read())
# with open('foo.txt') as f:
#     read_data = f.read()
# f.closed
# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('/bar.text', 'w') as b:
    b.write("now I have a machine gun")

# b = open('/bar.text', 'w')
# b.write("now I have a machine gun")
# b.write("ho")
# b.write("ho")
# b.write("ho")
# b.close()

# b = open('/bar.text', 'r')
# print(b.read())


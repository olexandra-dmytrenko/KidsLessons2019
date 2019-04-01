"""
Kids are to guess all the letters and their position.
Matrix works as Turing machine. Current letter and the next position are coded.
To find the second or next current letter
one should check the position of the following letter and as "current",
your current letter will be positioned.

As a homework kids are to change the letters and positions
codding their own words.
"""
print("DEBUG: Module '__main__.py' is executing")

from cli import main

#import pkg_resources
#
#filename = "__main__.py"
#filepath = pkg_resources.resource_filename(__name__, filename)
#print("DEBUG: Path: %s (__name__: %s)" % (filepath, __name__))

if __name__ == '__main__':
    main()

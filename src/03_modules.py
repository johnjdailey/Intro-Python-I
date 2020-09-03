


"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import platform
import sys
import getpass


# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE

print("On Unix, command line arguments are passed by bytes from OS. Python decodes them with filesystem encoding and “surrogateescape” error handler. When you need original bytes, you can get it by [os.fsencode(arg) for arg in sys.argv]")


# Print out the OS platform you're using:
# YOUR CODE HERE

print("OS Name:", os.name) 
print("Platform System:", platform.system())
print("Platform Release:", platform.release())


# Print out the version of Python you're using:
# YOUR CODE HERE

print("Python version:", sys.version)
print("Version info:", sys.version_info)


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE

print("Current Process ID (pid):", os.getpid())


# Print the current working directory (cwd):
# YOUR CODE HERE

print("Current Working Directory (cwd):", os.getcwd())


# Print out your machine's login name
# YOUR CODE HERE

print("Username:", getpass.getuser())

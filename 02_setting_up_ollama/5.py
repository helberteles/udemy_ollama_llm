# Title: Use Exec function to run a Code in String Type
#
# Description:
# This script demonstrates how to dynamically execute Python code that is stored
# inside a string variable. This is a powerful feature often used when building
# AI coding assistants, where the AI generates code as text and the system needs
# to run it.
#
# It also includes error handling (try-except) to prevent the program from
# crashing if the generated code contains bugs.
#
# Installation:
# No external libraries are needed for this script. 'random' is a built-in Python module.
#
# How to run this script:
# python 5.py

# Define a string variable named 'code'.
# This string contains valid Python code (importing random and printing a number).
# In a real AI application, this string would be the output from the LLM.
code = """
import random
print(random.randint(0,10))
"""

# The exec() function executes the string as if it were Python code.
# uncommenting line below would run it without safety checks:
# exec(code)


# It is best practice to wrap exec() in a try-except block.
# This ensures that if the code string has syntax errors or runtime errors,
# we can catch them gracefully instead of stopping the entire program.
try:
    # Execute the code stored in the string
    exec(code)
except Exception as e:
    # If an error occurs during execution, print the error message.
    print(f"Error executing generated code: {e}")

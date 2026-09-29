# Title: Get the Output of the Exec Function as a Variable
#
# Description:
# This script builds upon the previous concept of executing code strings.
# While 'exec()' runs the code, it normally prints the output directly to the console.
# In many AI applications, we need to CAPTURE that output into a variable so the AI
# can read it (e.g., to see the result of a calculation or a database query).
#
# This technique uses 'io.StringIO' and 'sys.stdout' to redirect the standard output.
#
# Installation:
# No external libraries are needed. 'io' and 'sys' are built-in Python modules.
#
# How to run this script:
# python 6.py

import io   # Used to create a memory buffer for text
import sys  # Used to access system-specific parameters and functions (like stdout)

# 1. Save the current standard output (the console).
# We need to restore this later so we can print to the screen again.
old_stdout = sys.stdout

# 2. Redirect standard output to a buffer.
# sys.stdout is where Python normally sends 'print()' statements.
# By setting it to 'buffer' (an io.StringIO object), anything printed
# will now go into this memory buffer instead of the console.
sys.stdout = buffer = io.StringIO()

# This is the code string we want to execute (simulating AI-generated code).
# It has a typo: 'random.randin' instead of 'random.randint' to demonstrate error handling.
code = """
import random
print(random.randin(0,10))
"""
# Note: The code above intentionally contains an error ('randin' instead of 'randint').

try:
    # 3. Execute the code.
    # The 'print' statement inside 'code' will now write to our 'buffer', not the screen.
    exec(code)
except Exception as e:
    # If the code fails (which it will, due to the typo), the error is caught here.
    # IMPORTANT: This print statement ALSO goes into the buffer because stdout is still redirected!
    print(f"Error executing generated code: {e}")

# 4. Restore standard output.
# We point sys.stdout back to the original console so we can see output again.
sys.stdout = old_stdout

# 5. Retrieve the captured content.
# .getvalue() extracts everything that was printed to the buffer.
output = buffer.getvalue()

# Finally, print the captured output to the real console.
print(output)

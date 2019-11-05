import os
import sys

program = "python"
arguments = ["called_process.py"]

print("Running the program")

os.execvp(program, (program,) + tuple(arguments))

# Note this line is not called. That is because the calling process
# is replaced by the called process. So when that finishes, we return
# to the command prompt
print("Goodbye")

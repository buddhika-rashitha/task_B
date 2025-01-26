# DA-108 : Python Programming - Task B
# Write a python program (script) which will slow down user input.

import time
import shutil

terminal_width = shutil.get_terminal_size().columns #linebreak based on terminal width
linebreak = ("━" * terminal_width) # Special Character (Box Drawings Heavy Horizontal - Unicode code point - U+2501)

title = "Task_B - Typing Timeout"
padding = (terminal_width - len(title)) // 2 # Calculate padding for centering
centered_title = " " * max(0, padding) + title
print(linebreak)
print(centered_title)

user_input = ""
while user_input.lower() != "q":
    print(linebreak)
    user_input = input("Enter something to slow down ('q' to quit): ")
    print(linebreak)
    
    if user_input.lower() == "q": # if user input either q or Q the program will quit
        print("Goodbye! Hope to see you again soon!")
        print(linebreak)
        break
    
    slowed_output = "... ".join(user_input.split()) + "..."
    print(slowed_output)
    time.sleep(1)  # Wait for 1 second before allowing new input

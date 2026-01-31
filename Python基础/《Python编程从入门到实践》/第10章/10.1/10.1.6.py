from pathlib import Path

path = Path('pi_string_1000.txt')
contents = path.read_text()

lines = contents.splitlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday in the form mmddyy: ")
if birthday in pi_string:
    print(f"Your birthday, {birthday}, appears in the first 1000 digits of pi.")
else:
    print(f"Your birthday, {birthday}, does not appear in the first 1000 digits of pi.")

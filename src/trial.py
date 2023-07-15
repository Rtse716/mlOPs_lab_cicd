from string import printable
import re

password = ""
if len(password) >= 8 and re.search('[a-zA-Z]', password) and re.findall('[^A-Za-z0-9]', password) and any(str.isdigit(c) for c in password):
    print(password)
else:
    print("Invalid password")
# and re.findall('[^A-Za-z0-9]',password)
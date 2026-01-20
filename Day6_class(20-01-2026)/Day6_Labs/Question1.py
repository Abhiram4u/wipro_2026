# 1. Uses re.match() to check whether a string starts with
#    a valid employee ID in the format EMP followed by 3 digits (e.g., EMP123)
import re
empId = "EMP123"

# print(re.match(r"^EMP\d{3}",empId))
print(bool(re.match(r"^[A-Z]{1,3}\d{3}", empId)))



# 2. Uses re.search() to find the
#    first occurrence of a valid email address in a given text

import re

text = "For support contact abhiramvarma069@gmail.com or sales@company.in"

pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

match = re.search(pattern, text)

if match:
    print("Email found:", match.group())
else:
    print("No email found")


# 3. Demonstrates the use of meta-characters (., *, +, ?) and
#    special sequences (\d, \w, \s) in the patterns


text = "Emp123 works 8 hours a day."

# Matches any single character except newline
print(re.search(r"E.p", text))      # Matches 'Emp'

# *  - 0 or more occurrences
print(re.search(r"\d*", text))      # Matches '' or digits at start

# +  - 1 or more occurrences
print(re.search(r"\d+", text))

# ?  - 0 or 1 occurrence
print(re.search(r"hours?", text))

# \d - Digit (0–9)
print(re.search(r"\d", text))

# \w - Word character (a–z, A–Z, 0–9, _)
print(re.search(r"\w+", text))

# \s - Whitespace (space, tab, newline)
print(re.search(r"\s", text))


# 4. Prints matched groups using capturing parentheses

text = "Employee ID: EMP123, Email: abhi.ram01@gmail.com"

pattern = r"(EMP\d{3}).*?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"

match = re.search(pattern, text)

if match:
    print("Full Match :", match.group(0))
    print("Group 1 (Employee ID):", match.group(1))
    print("Group 2 (Email):", match.group(2))
else:
    print("No match found")

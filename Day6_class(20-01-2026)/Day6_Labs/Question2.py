# # Topics Covered: Assertions, Regular expression modifiers
# Write a Python program that:

# 1.Validates a strong password using regular expressions with the following rules:

# Minimum 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one digit
# At least one special character
import re
password = input("Enter your password: ")

errors = []

if not re.search(r"[A-Z]", password):
    errors.append("Password must contain at least one uppercase letter")

if not re.search(r"[a-z]", password):
    errors.append("Password must contain at least one lowercase letter")

if not re.search(r"\d", password):
    errors.append("Password must contain at least one digit")

if not re.search(r"[@$!%*?&]", password):
    errors.append("Password must contain at least one special character")

if len(password) < 8:
    errors.append("Password must be at least 8 characters long")

# Final result
if errors:
    print("\nPassword is INVALID")
    for error in errors:
        print("-", error)
else:
    print("\nPassword is Valid")




# 3. Uses regular expression modifiers such as:
# re.IGNORECASE
text = "Hello Python"

print(re.search(r"python", text))
print(re.search(r"python", text, re.IGNORECASE))

# re.MULTILINE
text = """Hello
Python
World"""

print(re.findall(r"^P\w+", text))
print(re.findall(r"^P\w+", text, re.MULTILINE))

# re.DOTALL
text = "Hello\nPython"

print(re.search(r"Hello.*Python", text))
print(re.search(r"Hello.*Python", text, re.DOTALL))

#
# 4. Demonstrates how modifiers affect pattern matching with examples



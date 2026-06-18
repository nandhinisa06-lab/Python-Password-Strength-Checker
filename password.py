import re

# Get password from user
password = input("Enter your password: ")

score = 0
feedback = []

# Check length
if len(password) >= 8:
    score += 1
else:
    feedback.append("Use at least 8 characters.")

# Check uppercase letter
if re.search(r"[A-Z]", password):
    score += 1
else:
    feedback.append("Add at least one uppercase letter.")

# Check lowercase letter
if re.search(r"[a-z]", password):
    score += 1
else:
    feedback.append("Add at least one lowercase letter.")

# Check number
if re.search(r"\d", password):
    score += 1
else:
    feedback.append("Add at least one number.")

# Check special character
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1
else:
    feedback.append("Add at least one special character.")

# Classify password strength
if score == 5:
    strength = "Strong"
elif score >= 3:
    strength = "Medium"
else:
    strength = "Weak"

# Display result
print("\nPassword Strength:", strength)

if feedback:
    print("\nSuggestions to improve:")
    for item in feedback:
        print("-", item)
else:
    print("Excellent! Your password is secure.")
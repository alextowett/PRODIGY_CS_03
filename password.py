import re

def assess_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_char_criteria = bool(re.search(r'[@$!%*?&#]', password))

    # Strength level
    strength_level = 0

    # Assess criteria
    if length_criteria:
        strength_level += 1
    if uppercase_criteria:
        strength_level += 1
    if lowercase_criteria:
        strength_level += 1
    if digit_criteria:
        strength_level += 1
    if special_char_criteria:
        strength_level += 1

    # Feedback based on the strength level
    feedback = ""
    if strength_level == 5:
        feedback = "Your password is very strong."
    elif strength_level == 4:
        feedback = "Your password is strong."
    elif strength_level == 3:
        feedback = "Your password is moderate."
    elif strength_level == 2:
        feedback = "Your password is weak."
    else:
        feedback = "Your password is very weak."

    # Detailed criteria feedback
    if not length_criteria:
        feedback += "\n- Consider increasing the length to at least 8 characters."
    if not uppercase_criteria:
        feedback += "\n- Add at least one uppercase letter."
    if not lowercase_criteria:
        feedback += "\n- Add at least one lowercase letter."
    if not digit_criteria:
        feedback += "\n- Include at least one digit."
    if not special_char_criteria:
        feedback += "\n- Include at least one special character (e.g., @$!%*?&#)."

    return feedback

def main():
    print("Password Strength Assessor")
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)
    print("\n" + feedback)

if __name__ == "__main__":
    main()

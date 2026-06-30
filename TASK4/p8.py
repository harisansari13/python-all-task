def check_password(password):
    if len(password) >= 8:
        return "Strong Password"
    else:
        return "Weak Password"

print(check_password("python123"))
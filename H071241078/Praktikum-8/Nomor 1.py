import re

def validate_string(s):
    # Check if the string length is exactly 45 characters
    if len(s) != 45:
        return False
    
    # Extract the first 40 characters and the last 5 characters
    first_part = s[:40]
    last_part = s[40:]
    
    # Validate the first 40 characters (letters or even digits only)
    if not re.match(r"^[a-zA-Z02468]{40}$", first_part):
        return False
    
    # Validate the last 5 characters (odd digits or whitespace only)
    if not re.match(r"^[13579\s]{5}$", last_part):
        return False
    
    # If all conditions are met, the string is valid
    return True

# Menerima input dari pengguna
user_input = input("Masukkan string 45 karakter untuk divalidasi: ")

# Menampilkan hasil validasi
if validate_string(user_input):
    print("True")
else:
    print("False")

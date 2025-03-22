import random
def shuffle(strings):
    tempList = list(strings)
    random.shuffle(tempList)
    return ''.join(tempList)

def generate_password(length):
    if length < 8:
        return "Password should be at least 8 characters long"
    
    uppercase_letter = chr(random.randint(65, 90))  # One uppercase letter
    lowercase_letter = chr(random.randint(97, 122))  # One lowercase letter
    digit = chr(random.randint(48, 57))  # One digit
    special_character = chr(random.randint(33, 47))  # One special character
    
    remaining_chars = ''.join(chr(random.randint(33, 126)) for _ in range(length - 4))
    
    password = uppercase_letter + lowercase_letter + digit + special_character + remaining_chars
    
    return shuffle(password)

print(generate_password(8))
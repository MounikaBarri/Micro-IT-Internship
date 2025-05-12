import secrets
import string

def generate_password(length=12, uppercase=True, lowercase=True, digits=True, special=True):
    chars = []
    if uppercase: 
        chars += string.ascii_uppercase
    if lowercase: 
        chars += string.ascii_lowercase
    if digits: 
        chars += string.digits
    if special: 
        chars += string.punctuation  # Includes !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    
    if not chars:
        raise ValueError("At least one character type must be selected")
    
    # Ensure at least one character from each selected type
    password = []
    if uppercase: 
        password.append(secrets.choice(string.ascii_uppercase))
    if lowercase: 
        password.append(secrets.choice(string.ascii_lowercase))
    if digits: 
        password.append(secrets.choice(string.digits))
    if special: 
        password.append(secrets.choice(string.punctuation))
    
    # Fill remaining length
    remaining = length - len(password)
    password.extend(secrets.choice(chars) for _ in range(remaining))
    
    # Shuffle to avoid predictable patterns
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)
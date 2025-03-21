import base64
import hashlib
import os

def task_func(password, SALT_LENGTH=32):
    if not password:
        raise ValueError("Password cannot be None or empty")

    # Generate a random salt
    salt = os.urandom(SALT_LENGTH)

    # Hash the password using PBKDF2 HMAC with SHA-256
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256', 
        password.encode('utf-8'), 
        salt, 
        100000  # Number of iterations
    )

    # Encode the salt and the hashed password using base64
    salt_base64 = base64.b64encode(salt)
    hashed_password_base64 = base64.b64encode(hashed_password)

    return salt_base64, hashed_password_base64

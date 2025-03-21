import base64
from cryptography.fernet import Fernet

def task_func(message, encryption_key):
    # Ensure that the encryption key is the correct length for Fernet
    # Fernet keys must be 32 url-safe base64-encoded bytes
    if len(encryption_key) != 32:
        raise ValueError("Encryption key must be 32 characters long.")
    
    # Ensure the encryption key is properly formatted for Fernet
    fernet_key = base64.urlsafe_b64encode(encryption_key.encode('utf-8'))
    
    # Create a Fernet object
    fernet = Fernet(fernet_key)
    
    # Encrypt the message
    encrypted_message = fernet.encrypt(message.encode('utf-8'))
    
    # Encode the encrypted message with base64
    encoded_encrypted_message = base64.urlsafe_b64encode(encrypted_message).decode('utf-8')
    
    return encoded_encrypted_message

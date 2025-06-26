import secrets

def generate_secret_key():
    return secrets.token_hex(32)

def generate_password():
    return secrets.token_urlsafe(12)
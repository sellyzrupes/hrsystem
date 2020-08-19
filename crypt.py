from cryptography.fernet import Fernet
import config_variables

def encrypt_login_token(raw):
    return Fernet(str.encode(config.SECRET_KEY)).encrypt(str.encode(raw))

def decrypt_login_token(encrypted_token):
    return Fernet(str.encode(config.SECRET_KEY)).decrypt(encrypted_token).decode()

if __name__ == '__main__':
    #Validate encrypt decrypt
    print(decrypt_login_token(encrypt_login_token("Hello")))

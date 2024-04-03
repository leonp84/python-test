import hashlib
import os
import base64

import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


os.system("clear")


# # This is how password Hashing works / SHA-256 Algortith
user_password = 'witblad'
new_password = 'witblad'
x = hashlib.sha256(bytes(user_password.encode('utf-8'))).hexdigest()
y = hashlib.sha256(bytes(new_password.encode('utf-8'))).hexdigest()

print(x)
print(y)

if x == y:
    print('Passwords Match')
else:
    print('Try Again')

# Now for Encryption

# ** Generate Fernet Key based on user input of Master Password **

user_password = 'witblad'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=os.urandom(16),
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(bytes(user_password.encode('utf-8'))))

FKEY = Fernet(key)

# ** Encrypt and store password using Fernet Key **
new_password = "here-we-go"
new_enc_password = FKEY.encrypt(new_password.encode()).decode()
print(f"Encrypted Password: {new_enc_password}")

# ** Decrypt and display password using Fernet Key **
stored_dec_password = FKEY.decrypt(new_enc_password).decode()
print(f"Decrypted Password: {stored_dec_password}")






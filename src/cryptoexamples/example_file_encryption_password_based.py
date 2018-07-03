import base64
import os
import logging

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def file_encryption_password_based():
    """
    ENCRYPTION and DECRYPTION process
    TODO: Comments here
    """
    # alternative: read plain text from file
    plain_text = "Text that is going to be sent over an insecure channel and must be encrypted at all costs!\n" \
                 "Also with multiple lines!"

    # GENERATE password (not needed if you have a password already)
    password = b"mypassword"
    # TODO: Add password generation here

    # GENERATE random salt (needed for PBKDF2HMAC)
    salt = os.urandom(16)

    # DERIVE key (from password and salt)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # java example takes 256
        salt=salt,
        iterations=100000,  # java example takes 65536
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))

    # ENCRYPTION
    fernet = Fernet(key)
    cipher_text_bytes = fernet.encrypt(plain_text.encode('utf-8'))

    # WRITE to file
    with open("encrypted_file.enc", 'wb') as f:
        f.write(cipher_text_bytes)

    # READ from file
    with open("encrypted_file.enc", 'rb') as f:
        cipher_file_content = f.read()

    # DECRYPTION
    decrypted_cipher_text_bytes = fernet.decrypt(cipher_file_content)
    decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')

    logger.info("Decrypted and original plain text are the same: {}".format(decrypted_cipher_text == plain_text))

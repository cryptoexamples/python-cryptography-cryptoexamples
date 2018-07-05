import os
import logging

import secrets  # python >= 3.6
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def file_encryption_password_based():
    """
    All in one example for encryption and decryption of a file in one method.
    - Random key generation using OS random mode
    - Random salt generation using OS random mode
    - Key derivation using PBKDF2 HMAC SHA-512
    - AES-256 authenticated encryption using GCM
    - UTF-8 encoding of Strings
    """
    # TODO: read plain text from file
    plain_text = "Text that is going to be sent over an insecure channel and must be encrypted at all costs!\n" \
                 "Also with multiple lines!"

    # GENERATE password (not needed if you have a password already)
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = "".join(secrets.choice(alphabet) for _ in range(40))
    password = password.encode('utf-8')

    # GENERATE random salt (needed for PBKDF2HMAC)
    salt = os.urandom(16)

    # DERIVE key (from password and salt)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA512(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password)

    # GENERATE random nonce (number used once)
    nonce = os.urandom(32)

    # ENCRYPTION
    aesgcm = AESGCM(key)
    cipher_text_bytes = aesgcm.encrypt(
        nonce,
        plain_text.encode('utf-8'),
        None
    )

    # WRITE to file
    with open("encrypted_file.enc", 'wb') as f:
        f.write(cipher_text_bytes)

    # READ from file
    with open("encrypted_file.enc", 'rb') as f:
        cipher_file_content = f.read()

    # DECRYPTION
    decrypted_cipher_text_bytes = aesgcm.decrypt(
        nonce,
        cipher_file_content,
        None
    )
    decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')

    logger.info("Decrypted and original plain text are the same: {}".format(decrypted_cipher_text == plain_text))

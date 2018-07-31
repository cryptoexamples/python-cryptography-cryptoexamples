import logging
import os
import secrets  # python >= 3.6

from cryptography.exceptions import AlreadyFinalized
from cryptography.exceptions import InvalidTag
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def demonstrate_file_encryption_password_based(plain_text_file_name, password):
    """
    All in one example for encryption and decryption of a file in one method.
    - Random password generation using strong secure random number generator
    - Random salt generation using OS random mode
    - Key derivation using PBKDF2 HMAC SHA-512
    - AES-256 authenticated encryption using GCM
    - UTF-8 encoding of Strings
    - Exception handling
    """
    with open(plain_text_file_name, 'r') as plain_text_file:
        plain_text = plain_text_file.read()

    try:
        # GENERATE password (not needed if you have a password already)
        if not password:
            alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            password = "".join(secrets.choice(alphabet) for _ in range(40))
        password_bytes = password.encode('utf-8')

        # GENERATE random salt (needed for PBKDF2HMAC)
        salt = os.urandom(64)

        # DERIVE key (from password and salt)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=32,
            salt=salt,
            iterations=10000,
            backend=default_backend()
        )
        key = kdf.derive(password_bytes)

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
        with open("res/encrypted_file.enc", 'wb') as encrypted_file:
            encrypted_file.write(cipher_text_bytes)

        # READ from file
        with open("res/encrypted_file.enc", 'rb') as encrypted_file:
            cipher_file_content = encrypted_file.read()

        # DECRYPTION
        decrypted_cipher_text_bytes = aesgcm.decrypt(
            nonce,
            cipher_file_content,
            None
        )
        decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')

        logger.info("Decrypted and original plain text are the same: %s", decrypted_cipher_text == plain_text)
    except (UnsupportedAlgorithm, AlreadyFinalized, InvalidTag):
        logger.exception("Symmetric file encryption failed")


if __name__ == '__main__':
    # demonstrate method
    demonstrate_file_encryption_password_based("res/plain_text_file.txt", "")

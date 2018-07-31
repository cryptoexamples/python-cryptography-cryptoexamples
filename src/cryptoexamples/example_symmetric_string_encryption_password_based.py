import base64
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


def demonstrate_string_encryption_password_based(plain_text, password):
    """
    All in one example for encryption and decryption of a string in one method.
    - Random password generation using strong secure random number generator
    - Random salt generation using OS random mode
    - Key derivation using PBKDF2 HMAC SHA-512
    - AES-256 authenticated encryption using GCM
    - BASE64 encoding as representation for the byte-arrays
    - UTF-8 encoding of Strings
    - Exception handling
    """
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
        # CONVERSION of raw bytes to BASE64 representation
        cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)

        # DECRYPTION
        decrypted_cipher_text_bytes = aesgcm.decrypt(
            nonce,
            base64.urlsafe_b64decode(cipher_text),
            None
        )
        decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')

        logger.info("Decrypted and original plain text are the same: %s", decrypted_cipher_text == plain_text)
    except (UnsupportedAlgorithm, AlreadyFinalized, InvalidTag):
        logger.exception("Symmetric encryption failed")


if __name__ == '__main__':
    # demonstrate method
    demonstrate_string_encryption_password_based("Text that is going to be sent over an insecure channel and must be "
                                                 "encrypted at all costs!", "")

import base64
import logging
import os

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def demonstrate_string_encryption_key_based(plain_text):
    """
    All in one example for encryption and decryption of a string in one method.
    - Random key generation using OS random mode
    - AES-256 authenticated encryption using GCM
    - BASE64 encoding as representation for the byte-arrays
    - UTF-8 encoding of Strings
    - Exception handling
    """
    try:
        # GENERATE key
        key = AESGCM.generate_key(bit_length=256)

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
    except InvalidTag:
        logger.exception("Symmetric string encryption failed")


if __name__ == '__main__':
    # demonstrate method
    demonstrate_string_encryption_key_based("Text that is going to be sent over an insecure channel and must be "
                                            "encrypted at all costs!")

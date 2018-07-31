import base64
import logging

from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric import rsa

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def demonstrate_asymmetric_string_encryption(plain_text):
    """
    All in one example for asymmetric encryption and decryption of a string in one method.
    - Generation of public and private RSA 4096 bit keypair
    - RSA encryption and decryption of text using OAEP and MGF1 padding
    - BASE64 encoding as representation for the byte-arrays
    - UTF-8 encoding of Strings
    - Exception handling
    """
    try:
        # GENERATE NEW KEYPAIR
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # ENCRYPTION
        cipher_text_bytes = public_key.encrypt(
            plain_text.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA512()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        # CONVERSION of raw bytes to BASE64 representation
        cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)

        # DECRYPTION
        decrypted_cipher_text_bytes = private_key.decrypt(
            base64.urlsafe_b64decode(cipher_text),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA512()),
                algorithm=hashes.SHA512(),
                label=None
            )
        )
        decrypted_cipher_text = decrypted_cipher_text_bytes.decode('utf-8')

        logger.info("Decrypted and original plain text are the same: %s", decrypted_cipher_text == plain_text)
    except UnsupportedAlgorithm:
        logger.exception("Asymmetric encryption failed")


if __name__ == '__main__':
    # demonstrate method
    demonstrate_asymmetric_string_encryption("Text that is going to be sent over an insecure channel and must be "
                                             "encrypted at all costs!")

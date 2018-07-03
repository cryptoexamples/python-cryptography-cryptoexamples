import base64
import logging

from cryptography.fernet import Fernet

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def string_encryption_key_based():
    """
        ENCRYPTION and DECRYPTION process
        TODO: Comments here
        """
    plain_text = "Text that is going to be sent over an insecure channel and must be encrypted at all costs!"

    # GENERATE key
    key = Fernet.generate_key()

    # ENCRYPTION
    f = Fernet(key)
    cipher_text_bytes = f.encrypt(plain_text.encode('utf-8'))
    # CONVERSION of raw bytes to BASE64 representation
    cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)

    # DECRYPTION
    decrypted_text_bytes = f.decrypt(base64.urlsafe_b64decode(cipher_text))
    decrypted_text = decrypted_text_bytes.decode('utf-8')

    logger.info("Decrypted and original plain text are the same: {}".format(decrypted_text == plain_text))

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


def string_encryption_password_based():
    """
    ENCRYPTION and DECRYPTION process
    TODO: Comments here
    """
    plain_text = "Text that is going to be sent over an insecure channel and must be encrypted at all costs!"

    # GENERATE password (not needed if you have a password already)
    password = b"mypassword"
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for _ in range(40))
    password = password.encode('utf-8')
    # possible password generation (>=python 3.6), note that java example generates key

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
    # CONVERSION of raw bytes to BASE64 representation
    cipher_text = base64.urlsafe_b64encode(cipher_text_bytes)

    # DECRYPTION
    decrypted_text_bytes = fernet.decrypt(base64.urlsafe_b64decode(cipher_text))
    decrypted_text = decrypted_text_bytes.decode('utf-8')

    logger.info("Decrypted and original plain text are the same: {}".format(decrypted_text == plain_text))

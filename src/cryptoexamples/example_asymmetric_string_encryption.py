import base64
import logging

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def asymmetric_string_encryption():
    """
    ENCRYPTION and DECRYPTION process
    TODO: Comments here
    """
    plain_text = "Text that is going to be sent over an insecure channel and must be encrypted at all costs!"

    # TODO: load keypair?
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

    logger.info("Decrypted and original plain text are the same: {}".format(decrypted_cipher_text == plain_text))

import base64
import logging

from cryptography.exceptions import AlreadyFinalized
from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def demonstrate_string_hash(plain_text):
    """
    All in one example for hashing of a string in one method.
    - SHA-512 hashes
    - BASE64 encoding as representation for the byte-arrays
    - UTF-8 encoding of Strings
    - Exception handling
    """
    try:
        # Get digest instance
        digest = hashes.Hash(hashes.SHA512(), backend=default_backend())

        # CREATE HASH
        digest.update(plain_text.encode('utf-8'))
        hash_bytes = digest.finalize()

        # CONVERT/ENCODE IN BASE64
        hash_string = base64.urlsafe_b64encode(hash_bytes)

        logger.info(hash_string)
    except (UnsupportedAlgorithm, AlreadyFinalized):
        logger.exception("Hashing failed")


if __name__ == '__main__':
    # demonstrate method
    demonstrate_string_hash("Text that should be authenticated by comparing the hash of it!")

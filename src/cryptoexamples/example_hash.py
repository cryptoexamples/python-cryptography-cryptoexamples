import base64
import logging

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def string_hash():
    """
    HASHING process
    TODO: Comments here
    """
    plain_text = "Text that should be authenticated by comparing the hash of it!"

    # Get digest instance
    digest = hashes.Hash(hashes.SHA512(), backend=default_backend())

    # CREATE HASH
    digest.update(plain_text.encode('utf-8'))
    hash_bytes = digest.finalize()

    # CONVERT/ENCODE IN BASE64
    hash_string = base64.urlsafe_b64encode(hash_bytes)

    logger.info(hash_string)

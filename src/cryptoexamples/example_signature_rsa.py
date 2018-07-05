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


def signature_rsa():
    """
    All in one example for cryptographic signing of a string in one method.
    - Generation of public and private RSA 4096 bit keypair
    - SHA-512 with RSA signature of text using PSS and MGF1 padding
    - BASE64 encoding as representation for the byte-arrays
    - UTF-8 encoding of Strings
    """
    plain_text = "Text that should be signed to prevent unknown tampering with its content."

    # GENERATE NEW KEYPAIR
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    # SIGN DATA/STRING
    signature = private_key.sign(
        plain_text.encode('utf-8'),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA512()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA512()

    )
    logger.info("Signature: {}".format(base64.urlsafe_b64encode(signature)))

    # VERIFY JUST CREATED SIGNATURE USING PUBLIC KEY
    try:
        public_key.verify(
            signature,
            plain_text.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA512()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA512()
        )
        is_signature_correct = True
    except InvalidSignature:
        is_signature_correct = False

    logger.info("Signature is correct: {}".format(is_signature_correct))

import logging
import secrets  # python >= 3.6

from cryptography.exceptions import UnsupportedAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# set up logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def asymmetric_key_storage():
    """
    All in one example for key storage of a asymmetric key in one method.
    - Random password generation using strong secure random number generator
    - Generation of public and private RSA 4096 bit keypair
    - Serialization of the private key using PEM encoding, PKCS8 format and a password
    - Serialization of the public key using PEM encoding and Subject Public Key Info
    - Writing and loading of the keys
    - Exception handling
    """
    try:
        # GENERATE password (not needed if you have a password already)
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        password = "".join(secrets.choice(alphabet) for _ in range(20))
        logger.info(password)
        password_bytes = password.encode('utf-8')

        # GENERATE NEW KEYPAIR
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=4096,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # SERIALIZATION
        pem_private = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(password_bytes)
        )
        pem_public = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        # WRITE KEYS
        with open("private_key.pem", 'wb') as f:
            f.write(pem_private)
        with open("public_key.pem", 'wb') as f:
            f.write(pem_public)

        # LOAD KEYS
        with open("private_key.pem", "rb") as f:
            private_key_after = serialization.load_pem_private_key(
                f.read(),
                password=password_bytes,
                backend=default_backend()
            )
        with open("public_key.pem", "rb") as f:
            public_key_after = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )

        # CHECK whether keys are the same
        private_before = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        private_after = private_key_after.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_before = pem_public
        public_after = public_key_after.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        logger.info("Private Key before and after storage is the same: {}".format(private_before == private_after))
        logger.info("Public Key before and after storage is the same: {}".format(public_before == public_after))
    except (UnsupportedAlgorithm, ValueError, TypeError):
        logger.exception("Asymmetric key storage failed")

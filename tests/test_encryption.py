import os
import sys
# I need to add the path to PYTHONPATH so the files can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# by importing the module in each test function the code gets executed
from src.cryptoexamples.example_symmetric_string_encryption_password_based import demonstrate_string_encryption_password_based
from src.cryptoexamples.example_symmetric_string_encryption_key_based import demonstrate_string_encryption_key_based
from src.cryptoexamples.example_symmetric_file_encryption_password_based import demonstrate_file_encryption_password_based
from src.cryptoexamples.example_hash import demonstrate_string_hash
from src.cryptoexamples.example_asymmetric_string_encryption import demonstrate_asymmetric_string_encryption
from src.cryptoexamples.example_string_signature_rsa import demonstrate_signature_rsa
from src.cryptoexamples.example_asymmetric_key_storage import demonstrate_asymmetric_key_storage


def test_string_encryption_password_based(caplog):
    demonstrate_string_encryption_password_based("Text that is going to be sent over an insecure channel and must be "
                                                 "encrypted at all costs!", "")
    assert "Decrypted and original plain text are the same: True" in caplog.text


def test_string_encryption_key_based(caplog):
    demonstrate_string_encryption_key_based("Text that is going to be sent over an insecure channel and must be "
                                            "encrypted at all costs!")
    assert "Decrypted and original plain text are the same: True" in caplog.text


def test_file_encryption_password_based(caplog):
    demonstrate_file_encryption_password_based("res/plain_text_file.txt", "")
    assert "Decrypted and original plain text are the same: True" in caplog.text


def test_string_hash(caplog):
    import src.cryptoexamples.example_hash
    # uses string: "Text that should be authenticated by comparing the hash of it!"
    demonstrate_string_hash("Text that should be authenticated by comparing the hash of it!")
    assert "jg0X629-SmdP0_LTHZV_3zXBrizM3_hptRZVIuTXSCtyaqAe0NB8KMld2qebBIXFS1yowCUpCPu93l_fPmKEXg==" in caplog.text


def test_asymmetric_string_encryption(caplog):
    demonstrate_asymmetric_string_encryption("Text that is going to be sent over an insecure channel and must be "
                                             "encrypted at all costs!")
    assert "Decrypted and original plain text are the same: True" in caplog.text


def test_signature_rsa(caplog):
    demonstrate_signature_rsa("Text that should be signed to prevent unknown tampering with its content.")
    assert "Signature is correct: True" in caplog.text


def test_asymmetric_key_storage(caplog):
    demonstrate_asymmetric_key_storage("")
    assert "Private Key before and after storage is the same: True" in caplog.text
    assert "Public Key before and after storage is the same: True" in caplog.text

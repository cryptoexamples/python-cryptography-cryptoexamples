import os
import sys
# I need to add the path to PYTHONPATH so the file can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.cryptoexamples.example_string_encryption_password_based import string_encryption_password_based
from src.cryptoexamples.example_string_encryption_key_based import string_encryption_key_based
from src.cryptoexamples.example_file_encryption_password_based import file_encryption_password_based
from src.cryptoexamples.example_hash import string_hash

def test_string_encryption_password_based(caplog):
    string_encryption_password_based()
    assert "Decrypted and original plain text are the same: True" in caplog.text


def test_string_encryption_key_based(caplog):
    string_encryption_key_based()
    assert "Decrypted and original plain text are the same: True" in caplog.text


def test_file_encryption_password_based(caplog):
    file_encryption_password_based()
    assert "Decrypted and original plain text are the same: True" in caplog.text


def test_string_hash(caplog):
    string_hash()
    # uses string: "Text that should be authenticated by comparing the hash of it!"
    assert "jg0X629-SmdP0_LTHZV_3zXBrizM3_hptRZVIuTXSCtyaqAe0NB8KMld2qebBIXFS1yowCUpCPu93l_fPmKEXg==" in caplog.text

import os
import sys
# I need to add the path to PYTHONPATH so the file can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.cryptoexamples.example_string_encryption_password_based import string_encryption_password_based


def test_string_encryption_password_based(caplog):
    string_encryption_password_based()
    assert "Decrypted and original plain text are the same: True" in caplog.text

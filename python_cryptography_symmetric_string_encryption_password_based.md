---
title: Python Symmetric Password Based String Encryption using Cryptography
keywords: sample
summary: "Password based symmetric string encryption in Python"
permalink: python_cryptography_symmetric_string_encryption_password_based.html
folder: Python Cryptography
references: [
    # Place a list of references used to create and/or understand this example.
    {
        url: "https://cryptography.io/en/latest/hazmat/primitives/aead/#cryptography.hazmat.primitives.ciphers.aead.AESGCM",
        description: "Cryptography AEAD Documentation - AESGCM"
    },
    {
        url: "https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/#cryptography.hazmat.primitives.kdf.pbkdf2.PBKDF2HMAC",
        description: "Cryptography Password Based Key Derivation Function 2 Documentation"
    }
]
authors: [
    {
        name: "Manuel Kloppenburg",
        url: "https://github.com/mklopp"
    }
]
# List all reviewers that reviewed this version of the example. When the example is updated all old reviews
# must be removed from the list below and the code has to be reviewed again. The complete review process
# is documented in the main repository of CryptoExamples
current_reviews: [

]
# Indicates when this example was last updated/created. Reviews don't change this.
last_updated: "2018-07-12"
tags: [Python, AES, GCM, PBKDF2, Salt, AEAD]
---

## Use cases

- Password based encryption of a string
- Previously shared common secret (password)

## Installation

[Install](https://cryptography.io/en/latest/installation/) `cryptography` with [`pip`](https://packaging.python.org/tutorials/installing-packages/): `pip install cryptorgraphy`

## Used Python version

- Python 3.6
- Python 3.7

## Example Code for Python based symmetric encryption using AES-GCM and PBKDF2

```python
{% include_relative src/cryptoexamples/example_symmetric_string_encryption_password_based.py %}
```



{% include links.html %}

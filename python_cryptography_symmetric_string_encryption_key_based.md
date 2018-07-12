---
title: Python Symmetric String Encryption with key generation using Cryptography
keywords: sample
summary: "Symmetric string encryption in Python with key generation"
permalink: python_cryptography_symmetric_string_encryption_key_based.html
folder: Python Cryptography
references: [
    # Place a list of references used to create and/or understand this example.
    {
        url: "https://cryptography.io/en/latest/hazmat/primitives/aead/#cryptography.hazmat.primitives.ciphers.aead.AESGCM",
        description: "Cryptography AEAD Documentation - AESGCM"
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
tags: [Python, AES, GCM, Salt, AEAD]
---

## Use cases

- Random key generation
- Key based encryption of a string

## Installation

[Install](https://cryptography.io/en/latest/installation/) `cryptography` with [`pip`](https://packaging.python.org/tutorials/installing-packages/): `pip install cryptorgraphy`

## Used Python version

- Python 3.6
- Python 3.7

## Example Code for Python based symmetric encryption using AES-GCM and generation of keys

```python
{% include_relative src/cryptoexamples/example_symmetric_string_encryption_password_based.py %}
```



{% include links.html %}

---
title: Python Asymmetric String Encryption using Cryptography
keywords: sample
summary: "Asymmetric String Encryption in Python"
permalink: python_cryptography_asymmetric_string_encryption.html
folder: Python Cryptography
references: [
    # Place a list of references used to create and/or understand this example.
    {
        url: "https://cryptography.io/en/latest/hazmat/primitives/asymmetric/rsa/",
        description: "Cryptography RSA Documentation"
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
tags: [Python, RSA, Asymmetric, String, Encryption]
---

## Use cases

- All can encrypt a message using the public key, but only the recipient can decrypt it using the private key
- Encrypt a string using the public key and decrypting it using the private key

## Installation

[Install](https://cryptography.io/en/latest/installation/) `cryptography` with [`pip`](https://packaging.python.org/tutorials/installing-packages/): `pip install cryptorgraphy`

## Used Python version

- Python 3.6
- Python 3.7

## Example Code for Python based asymmetric encryption using RSA

```python
{% include_relative src/cryptoexamples/example_asymmetric_string_encryption.py %}
```

{% include links.html %}

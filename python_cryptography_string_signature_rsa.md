---
title: Python String Signing using Cryptography
keywords: sample
summary: "String signing in Python"
permalink: python_cryptography_string_signature_rsa.html
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
tags: [Python, RSA, Asymmetric, String, hash, SHA, SHA-512]
---

## Use cases

- Verifying if a string has been changed

## Installation

[Install](https://cryptography.io/en/latest/installation/) `cryptography` with [`pip`](https://packaging.python.org/tutorials/installing-packages/): `pip install cryptorgraphy`

## Used Python version

- Python 3.6
- Python 3.7

## Example Code for Python based signing of a String using SHA-512, RSA 4096, BASE64 and UTF-8 encoding

```python
{% include_relative src/cryptoexamples/example_string_signature_rsa.py %}
```



{% include links.html %}

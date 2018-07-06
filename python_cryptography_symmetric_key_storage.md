---
title: Python Asymmetric Key Storage using Cryptography
keywords: sample
summary: "Asymmetric key storage in Python"
permalink: python_cryptography_asymmetric_key_storage.html
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
last_updated: "2018-07-06"
tags: [Python, RSA, Asymmetric, Key, Storage, Serialization, PEM]
---

## Use cases

- Store private and public keys as files

## Sample Code for Python based asymmetric key storage using PEM serialization

```python
{% include_relative src/cryptoexamples/example_asymmetric_key_storage.py %}
```

{% include links.html %}
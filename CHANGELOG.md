# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Fixed
- Fixed usage of SHA512 instead of SHA256
## [0.3.0] - 2018-09-10

### Added

- added a custom checker for pylint to check the guidelines

### Changed

- changed travis to use pylint on python 3.7 as well
- changed the password in all valid functions to be optional
- changed the examples to use random.SystemRandom instead of secrets module
- added support for python 2.7
- change MG1 hash functions to SHA-256
- change nonce for AESGCM to 12 bytes
- change signing and verification hash functions zo SHA-256
- change all functions with multiple parameter to use named parameters
- change pylint to only allow lines with max 100 characters

### Fixed

- fixed a link in the README pointing to the old repository

## [0.2.0] - 2018-08-07

### Added 

- added python 3.7 to travis
- added valid python versions in each example markdown page
- added install instructions in each example markdown page
- added pylint

### Changed

- changed logging to lazy logging
- changed salt to 64 bytes for symmetric encryption
- changed iterations to 10000 for symmetric encryption
- changed functions to have demonstrate_ prefix
- changed functions to be parameterized
- changed file encryption to use a file instead of text

## [0.1.1] - 2018-07-11

### Changed

- fixed wrong link to rsa signature file on landing page

## [0.1.0] - 2018-07-06

### Added

- added Changelog
- added Asymmetric RSA String Encryption
- added Asymmetric RSA String Signature
- added Asymmetric RSA Key Storage
- added Symmetric key based String Encryption
- added Symmetric password based String Encryption
- added Symmetric password based File Encryption
- added Hashing
- added testing

## [X.Y.Z] - XXXX-XX-XX (TEMPLATE for new versions)

### Added

- added something
- added something else

### Changed

- changed something
- changed something else

### Deprecated

- deprecated something
- deprecated something else

### Removed

- removed something
- removed something else

### Fixed

- fixed something
- fixed something else

### Security

- made some security relevant changes
- made other security relevant changes

[Unreleased]: https://github.com/cryptoexamples/python-cryptography-cryptoexamples/compare/v0.3.0...HEAD
[0.3.0]: https://github.com/cryptoexamples/java-crypto-examples/releases/tag/v0.3.0
[0.2.0]: https://github.com/cryptoexamples/java-crypto-examples/releases/tag/v0.2.0
[0.1.1]: https://github.com/cryptoexamples/java-crypto-examples/releases/tag/v0.1.1
[0.1.0]: https://github.com/cryptoexamples/java-crypto-examples/releases/tag/v0.1.0

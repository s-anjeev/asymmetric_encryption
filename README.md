# RSA Encryption and Decryption Script

This Python script demonstrates RSA encryption and decryption using the `rsa` module. It assumes that you have already generated public and private keys using a script named `asymmetric_keys.py`. The script reads the public key from "public.pem" and the private key from "private.pem". It then encrypts a message using the public key and writes the encrypted data to a file named "encrypted.data". After that, it decrypts the data using the private key and writes the decrypted data to a file named "decrypted.data".

## Prerequisites

- Python 3.x
- The `rsa` module (install it using `pip install rsa`)

## Usage

1. Run the `asymmetric_keys.py` script to generate public and private key pairs.
2. Ensure that the generated public key is saved in a file named `public.pem` and the private key is saved in a file named `private.pem`.
3. Run the `symmetric.py` script to perform encryption and decryption.

```bash
python symmetric.py
```

## File Descriptions
1. public.pem: Contains the public key for encryption.
2. private.pem: Contains the private key for decryption.
3. encrypted.data: Stores the encrypted data after encryption.
4. decrypted.data: Stores the decrypted data after decryption.

## Contributing

If you have suggestions, enhancements, or encounter issues, feel free to open an issue or submit a pull request.
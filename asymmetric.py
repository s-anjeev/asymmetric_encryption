# in this script we are using public and private keys that we have created using asymmetric_key.py
# so to use this script first obtain public and private keys by running asymmetric_key.py
import rsa

# encrypt data using public key
def encrypt_data(message,public_key):
    try:
        encrypted_data = rsa.encrypt(message.encode(),public_key)
        # write encrypted data into encrypted.data
        with open("encrypted.data","wb") as file:
            file.write(encrypted_data)
    except Exception as e:
        print(f"Error during encryption: {e}")

# decrypt data using public key
def decrypt_data(encrypted_data, private_key):
    try:
        decrypted_data = rsa.decrypt(encrypted_data, private_key)
        # write decrypted data into decrypted.data
        with open("decrypted.data","wb") as file:
            file.write(decrypted_data)
    except Exception as e:
        print(f"Error during decryption: {e}")

# read public key from public.pem
try:
    with open("public.pem","rb") as file:
        public_key = rsa.PublicKey.load_pkcs1(file.read())
except FileNotFoundError:
    print("Public key file not found")
except Exception as e:
    print(f"Error loading public ke: {e}")

# read private key from private.pem
try:
    with open("private.pem","rb") as file:
        private_key = rsa.PrivateKey.load_pkcs1(file.read())
except FileNotFoundError:
    print("Private key file not found.")
    exit()
except Exception as e:
    print(f"Error loading private key: {e}")
    exit()

if __name__ == "__main__":
    # message to be encrypted
    message = "Hello, I am implementing RSA."
    # encrypt
    encrypt_data(message,public_key)
    # decrypt
    try:
        encrypted_data = open("encrypted.data", "rb").read()
        decrypt_data(encrypted_data, private_key)
    except FileNotFoundError:
        print("Encrypted data file not found.")
    except Exception as e:
        print(f"Error during decryption: {e}")
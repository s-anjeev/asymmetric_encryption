# in this script we are generating public and private keys for symmeric encryption
# keys will be saved into files so that they can be used later, and we dont need to generate new key everytime
import rsa

def generate_key(bytes):
    try:
        public_key, private_key = rsa.newkeys(bytes)
    except Exception as e:
        print("Error while generating keys: {e}")
    # we are using PEM (Privacy Enhanced Mail) files to store public and private keys
    # PEM files are ASCII-encoded, making them human-readable
    with open("public.pem","wb") as f:
        # Write the PEM-formatted public key to the file.
        f.write(public_key.save_pkcs1("PEM"))

    with open("private.pem","wb") as f:
        # Write the PEM-formatted public key to the file.
        f.write(private_key.save_pkcs1("PEM"))
    
if __name__ == "__main__":
    bytes = 1024
    generate_key(bytes)
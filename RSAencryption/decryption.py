import rsa

# loading up the private key
with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# loading up the encrypted message
encrypted_message= open("encrypted.message", "rb").read()
# decrypting the encrypted message
decrypted_message = rsa.decrypt(encrypted_message, private_key)

print(decrypted_message.decode())
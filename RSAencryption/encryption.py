import rsa

# opens in read-binary mode since it is stored in binary formate
with open("public.pem", "rb") as f:
    
    #This method takes the raw byte data (in PKCS#1 format) 
    #and converts it back into a usable RSA public key object, 
    public_key = rsa.PublicKey.load_pkcs1(f.read())


with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# this is the message that we will be encrypted and later decrypted
message = "this is message was encrypted"

# encryptes the message using the public key 
encrypted_message = rsa.encrypt(message.encode(), public_key)
print(encrypted_message)

# stores the encrypted message in a file to be extracted later and decrypted
with open("encrypted.message", "wb") as f:
    f.write(encrypted_message)

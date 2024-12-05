import rsa

# This function generates a pair of RSA keys,
# a public key and a private key with a key length of 1024 bits.
public_key, private_key = rsa.newkeys(1024)


# This line opens/creates a file called public.pem
# in write-binary mode
# This specifies that the file is opened in binary mode, 
# which means that data will be written as bytes, not as plain text.
with open("public.pem", "wb") as f:

    
#public_key.save_pkcs1("PEM") converts the RSA public key to a PKCS#1 format, which structures the key in a standardized way.
#Then, it encodes this PKCS#1-formatted key into PEM, a readable text format
#Finally, f.write(...) writes this PEM-encoded text to the file, 
#allowing you to save and later share the key in a commonly used format
    f.write(public_key.save_pkcs1("PEM"))


with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

    
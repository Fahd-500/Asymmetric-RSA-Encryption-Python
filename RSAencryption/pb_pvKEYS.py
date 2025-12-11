import rsa

# This function generates a pair of RSA keys,
# a public key and a private key with a key length of 1024 bits.
public_key, private_key = rsa.newkeys(1024)


# This line opens/creates a file called public.pem
with open("public.pem", "wb") as f:

#public_key.save_pkcs1("PEM") converts the RSA public key to a PKCS#1 format, which structures the key in a standardized way.
#Then, it encodes this PKCS#1-formatted key into PEM, a readable text format
    f.write(public_key.save_pkcs1("PEM"))


with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))

    

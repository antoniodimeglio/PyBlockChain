from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from os import path


def createStoreKeys(): #function that generates both a private and public key
    
    privateKey = ""

    publicKey = ""


    if (path.exists('privateKey.pem') == False or path.exists('publicKey.pem') == False): #looks for the private and public key
        privateKey = rsa.generate_private_key(  #Generating private key
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
        )
        publicKey = privateKey.public_key() #Generating public key

        pem = privateKey.private_bytes( #object used to serialize key
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
        )

        with open('privateKey.pem', 'wb+') as f: #writing key on file 
            f.write(pem)

        pem = publicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        with open('publicKey.pem', 'wb+') as f:
            f.write(pem)
    else: #if the file holding keys are found they get loaded
        with open('privateKey.pem', 'rb') as f:
            privateKey = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )
        with open('publicKey.pem', 'rb') as f:
            publicKey = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )

    return (privateKey, publicKey)





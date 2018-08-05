import os
from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PublicKey 
##### ^ Need this to generate an elliptic-curve-compatible public key.
import cryptography.hazmat.primitives.asymmetric.dsa 
##### ^ To digitally sign messages
##### Both X25519PrivateKey and X25519PublicKey call the backend class with 
##### from cryptography.hazmat.backends.openssl.backend import backend 
##### Is this library or class vulnerable to any known OpenSSL vulnerabilities?

# def RSA_private_key():
#   return rsa.generate_private_key(
#     public_exponent = 65537,
#     key_size = 2048,
#     backend = default_backend()
#     )

def private_key():
  return X25519PrivateKey.generate()

def public_key():
  return X25519PublicKey.generate()
##### ^ Generate an EC-compatible public key.  

def get_shared_key(privKey, peerPubKey):
  return privKey.exchange(peerPubKey)
#####
##### def get_private_DSA_key(prime_modulus):
#####  return DSAParameters(self)
##### ^ Returns a DSA private key
##### https://cryptography.io/en/latest/_modules/cryptography/hazmat/primitives/asymmetric/dsa/#generate_private_key


#derivation function: HKDF
#https://cryptography.io/en/latest/hazmat/primitives/key-derivation-functions/?highlight=HKDF#cryptography.hazmat.primitives.kdf.hkdf.HKDF
def get_derived_key(info, sharedKey):
  salt = os.urandom(16)
  return HKDF(
     algorithm=hashes.SHA256(),
     length=32,
     salt = salt,
     info = info,
     # python3:
     # salt=bytes(salt, encoding='utf8'),
     # info=bytes(info, encoding='utf8'),
     backend=default_backend()
 ).derive(sharedKey)

def handshake(sender_name):
  # In a real handshake the pubkey_receiver will be received from the
  # other party. For this example we'll generate some arbitrary private and public keys.
  # Note that in a DH handshake both peers must agree on a common set of parameters.
  privkey_sender = private_key()
  pubkey_sender = privkey_sender.public_key()

  privkey_receiver = private_key()
  pubkey_receiver = privkey_receiver.public_key()

  shared_key = get_shared_key(privkey_sender, pubkey_receiver)
  derived_key = get_derived_key(sender_name, shared_key)
  return derived_key

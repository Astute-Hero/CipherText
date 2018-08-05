import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

def encrypt(key, plaintext, associated_data):
  ##### Line 8: Does associated_data need to be a required parameter?
  aesgcm = AESGCM(key)
  ##### Line 10: What does AESGCM do? 
  nonce = os.urandom(16) #never reuse a nonce with a key
  ##### Line 10: Need to convert this to type int or bytes. Also need to ensure it is an 
  ##### adequate random number (Do we need a large prime? If so test for primality.
  ##### Do we need a safe prime? Do we need a composite number n = pq, for large
  ##### primes p, q?)
  #associated_data is authenticated with the key but not encrypted.
  ciphertext = aesgcm.encrypt(nonce, plaintext, associated_data)
  return (aesgcm, nonce, ciphertext)

def decrypt(aesgcm, nonce, ciphertext, associated_data):
  return aesgcm.decrypt(nonce, ciphertext, associated_data)

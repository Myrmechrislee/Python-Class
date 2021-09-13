import hashlib, binascii
text = "hello"

# 1. a) Calculate SHA-224 Hash of text
hash_str = binascii.hexlify(hashlib.sha224(text.encode("ascii")).digest()).decode()
print("SHA-224(\"{0}\")={1}".format(text, hash_str))

# 1. b) check integrety with "ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193".
print("Integrety = " + str(hash_str == "ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193"))

# 2. a) Calculate SHA-256 Hash of text
hash_str = binascii.hexlify(hashlib.sha256(text.encode("ascii")).digest()).decode()
print("SHA-256(\"{0}\")={1}".format(text, hash_str))

# 2. b) check integrety with "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824".
print("Integrety = " + str(hash_str == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"))

# 3. a) Calculate SHA3-224 Hash of text
hash_str = binascii.hexlify(hashlib.sha3_224(text.encode("ascii")).digest()).decode()
print("SHA-256(\"{0}\")={1}".format(text, hash_str))

# 3. b) check integrety with "b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81".
print("Integrety = " + str(hash_str == "b87f88c72702fff1748e58b87e9141a42c0dbedc29a78cb0d4a5cd81"))

# 4. a) Calculate SHA3-384 Hash of text
hash_str = binascii.hexlify(hashlib.sha3_384(text.encode("ascii")).digest()).decode()
print("SHA-256(\"{0}\")={1}".format(text, hash_str))

# 4. b) check integrety with "720aea11019ef06440fbf05d87aa24680a2153df3907b23631e7177ce620fa1330ff07c0fddee54699a4c3ee0ee9d887".
print("Integrety = " + str(hash_str == "720aea11019ef06440fbf05d87aa24680a2153df3907b23631e7177ce620fa1330ff07c0fddee54699a4c3ee0ee9d887"))

# 5. a) Calculate Keccak-384 Hash of text
from Crypto.Hash import keccak
import binascii
hash_str = binascii.hexlify(keccak.new(data=text.encode("ascii"), digest_bits=384).digest()).decode()
print("KECCAK-384(\"{0}\")={1}".format(text, hash_str))

# 5. b) check integrety with "dcef6fb7908fd52ba26aaba75121526abbf1217f1c0a31024652d134d3e32fb4cd8e9c703b8f43e7277b59a5cd402175".
print("Integrety = " + str(hash_str == "dcef6fb7908fd52ba26aaba75121526abbf1217f1c0a31024652d134d3e32fb4cd8e9c703b8f43e7277b59a5cd402175"))

# 6. a) Calculate Whirlpool (512 Bit) Hash of text
hash_str = binascii.hexlify(hashlib.new("whirlpool", text.encode("ascii")).digest()).decode()
print("whilpool(\"{0}\")={1} (512)".format(text, hash_str))

# 6. b) check integrety with "0a25f55d7308eca6b9567a7ed3bd1b46327f0f1ffdc804dd8bb5af40e88d78b88df0d002a89e2fdbd5876c523f1b67bc44e9f87047598e7548298ea1c81cfd73"
print("Integrety = " + str(hash_str == "0a25f55d7308eca6b9567a7ed3bd1b46327f0f1ffdc804dd8bb5af40e88d78b88df0d002a89e2fdbd5876c523f1b67bc44e9f87047598e7548298ea1c81cfd73"))
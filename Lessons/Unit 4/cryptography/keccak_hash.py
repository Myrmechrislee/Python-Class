from Crypto.Hash import keccak
import binascii
text = b"hello"
keccak256 = keccak.new(data=text, digest_bits=256).digest()
print("keccak256(\"" + text.decode() + "\")=" + binascii.hexlify(keccak256).decode())
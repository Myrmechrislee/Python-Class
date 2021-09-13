import hmac, binascii, hashlib

# Write a program to calculate HMAC-SHA-384 of given text message by given key. 


#1. a) convert the following data to hmac
# Message: "hello"
# Key: "cryptography"
message = "hello"
key = "cryptography"
hashed = hmac.new(key.encode("ascii"), message.encode("ascii"), hashlib.sha384).digest()
print("hmac('{0}', '{1}')={2}".format(message, key, binascii.hexlify(hashed).decode()))

#1. b) check integrety "83d1c3d3774d8a32b8ea0460330c16d1b2e3e5c0ea86ccc2d70e603aa8c8151d675dfe339d83f3f495fab226795789d4"
print("Integrety = " + str(binascii.hexlify(hashed).decode() == "83d1c3d3774d8a32b8ea0460330c16d1b2e3e5c0ea86ccc2d70e603aa8c8151d675dfe339d83f3f495fab226795789d4"))

#1. a) convert the following data to hmac
# Message: "hello"
# Key: "again"
message = "hello"
key = "again"
hashed = hmac.new(key.encode("ascii"), message.encode("ascii"), hashlib.sha384).digest()
print("hmac('{0}', '{1}')={2}".format(message, key, binascii.hexlify(hashed).decode()))

#1. b) check integrety "4c549a549aa037e0fb651569bf271faa23cfa20e8a9d21438a6ff5bf6be916bebdbaa48001e0cd6941ec74cd02be70e5"
print("Integrety = " + str(binascii.hexlify(hashed).decode() == "4c549a549aa037e0fb651569bf271faa23cfa20e8a9d21438a6ff5bf6be916bebdbaa48001e0cd6941ec74cd02be70e5"))

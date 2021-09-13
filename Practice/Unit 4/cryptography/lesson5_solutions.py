import hmac, hashlib, binascii

# start = hashlib.sha256(b"hello").digest()

# outputs = []

# for n in range(30):
#     hash = hmac.new(bytearray([n]), start, hashlib.sha256).digest()
#     big = int.from_bytes(hash, "big")
#     rand = 1 + big % 10
#     outputs.append(rand)

# print(outputs)

# start = hashlib.sha256(b"random text").digest()

# outputs = []
# for n in range(30):
#     hash_256 = hmac.new(bytearray([n]), start, hashlib.sha256).digest()
#     big = int.from_bytes(hash_256, "big")
#     rand = 1 + big % 10
#     outputs.append(str(rand))

# print(str.join(" ", outputs))


start = hashlib.sha256(b"fun").digest()
output = []

for n in range(30):
    hash = hmac.new(bytearray([n]), start, hashlib.sha256).digest()
    big = int.from_bytes(hash, "big")
    rand = 1 + big % 10
    output.append(str(rand))

print(str.join(" ", output))
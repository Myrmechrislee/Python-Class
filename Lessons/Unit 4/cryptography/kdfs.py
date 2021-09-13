import os, binascii
from backports.pbkdf2 import pbkdf2_hmac

# salt = binascii.unhexlify('aaef2d3f4d77ac66e9c5a6c3d8f921d1')
# password = "p@$Sw0rD~1".encode("utf8")
# key = pbkdf2_hmac("sha256", password, salt, 500000, 32)
# print("Derived Key =" + binascii.hexlify(key).decode())
# print("Integrety = " + str(key == binascii.unhexlify("52c5efa16e7022859051b1dec28bc65d9696a3005d0f97e506c42843bc3bdbc0")))

import pyscrypt
# salt = b'aa1f2d3f4d23ac44e9c5a6c3d8f9ee8c'
# passwd = b'p@$Sw0rD~7'
# key = pyscrypt.hash(passwd, salt, 2048, 8, 1, 32)
# print("Derived key:", key.hex())
# print("Integrety = " + str(key.hex() == "e813a6f6ccc4e9110193bf9efb7c0a489d76655f9e36629dccbeaf2a73bc0c6f"))
# config = "16384$8$1$kytG1MHY1KU=$afc338d494dc89be40e317788e3cd9166d066709db0e6481f0801bd918710f46".split("$")
# pswd = "p@ss~123"
# derived_key = pyscrypt.hash(
#     pswd.encode("ascii"),
#     config[3].encode("ascii"),
#     int(config[0]),
#     int(config[1]),
#     int(config[2]),
#     32
# )
# print("Derived key =\t" + derived_key.hex())
# print("Actual Key =\t" + config[4])

import argon2, binascii
password = "password"
salt = "some salt"
hash = argon2.hash_password_raw(
    password.encode("ascii"),
    salt=salt.encode("ascii"),
    time_cost=16,
    parallelism=2,
    hash_len=32,
    type=argon2.low_level.Type.ID
)
print("Argon2 raw hash:", binascii.hexlify(hash))

a2_hasher = argon2.PasswordHasher(time_cost=16, parallelism=1, hash_len=32, encoding="ascii")
p_hash = a2_hasher.hash(password)
print("Argon2 hash (random salt):", p_hash)

logged_in = False
while not logged_in:
    password = input("Password: ")
    try:
        print("Argon2 verify (correct password):", a2_hasher.verify(p_hash, password))
        logged_in = True
    except:
        print("Argon2 verify (correct password):", False)
print("Success")
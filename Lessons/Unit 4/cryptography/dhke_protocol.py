import pyDHE

alice = pyDHE.new(group=18)
alicePK = alice.getPublicKey()
print("Alice public key:", alicePK)

bob = pyDHE.new(group=14)
bobPK = bob.getPublicKey()
print("Bob public key:", bobPK)

print("Now exchange the public keys (e.g. through Internet)")

aliceSK = alice.update(bobPK)
print("Alice shared key:", aliceSK)

bobSK = bob.update(alicePK)
print("Bob shared key:", bobSK)

print("Equal shared keys:", aliceSK == bobSK)
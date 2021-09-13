import os

def rand_int(min, max):
    return min + int.from_bytes(os.urandom(32), "big") % (max - min + 1)

class Alice:
    def __init__(self, g=3, prime=13):
        self.secret = rand_int(1, 10)
        print("Alice initialised p=%i prime=%i and secret=%i" % (g, prime, self.secret))
        self.prime = prime
        self.g = g
        self.public = g ** self.secret % prime
        print("Alice public = %i^%i mod %i = " % (g, self.secret, prime) + str(self.secret))
    def get_shared_secret(self, b_public: int):
        self.shared_secret = b_public ** self.secret % self.prime
        print("Alice shared secret = %i ^ %i mod %i = %i" % (b_public, self.secret, self.public, self.shared_secret))

class Bob:
    def __init__(self, g=3, prime=13) -> None:
        self.secret = rand_int(1, 10)
        print("Bob initialised p=%i prime=%i and secret=%i" % (g, prime, self.secret))
        self.prime = prime
        self.g = g
        self.public = g ** self.secret % prime
        print("Alice public = %i^%i mod %i = " % (g, self.secret, prime) + str(self.secret))
    def get_shared_secret(self, a_public: int):
        self.shared_secret = a_public ** self.secret % self.prime
        print("Bob shared secret = %i ^ %i mod %i = %i" % (a_public, self.secret, self.public, self.shared_secret))

alice = Alice()
bob = Bob()
print("Alice Public -> Bob")
bob.get_shared_secret(alice.public)
print("Bob Public -> Alice")
alice.get_shared_secret(bob.public)
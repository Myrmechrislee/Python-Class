import hashlib, binascii
text = b"hello"

def p(a):
    try:
        print("{0}(\"{1}\")={2}".format(a, text.decode(), hashlib.new(a).hexdigest()))
    except Exception as e:
        print("{0}(\"{1}\", 256)={2}".format(a, text.decode(), hashlib.new(a).hexdigest(256)))

for algorithm in hashlib.algorithms_available:
    p(algorithm)
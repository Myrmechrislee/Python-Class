import hashlib, hmac, binascii

key = b"1234"
msg = b"hello"

print(binascii.hexlify(hmac.new(key, msg, hashlib.sha256).digest()).decode())
"920a89da93cbbe3dfe70788d42daec47b58ba97450a81f03646d589797657010"
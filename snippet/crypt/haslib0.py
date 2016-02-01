import hashlib
import hashlib, binascii

m = hashlib.md5()
m.update("Nobody inspects")
m.update(" the spammish repetition")
hd = m.hexdigest()
print(hd)
m.digest_size
m.block_size


h = hashlib.new('ripemd160')
h.update("Nobody inspects the spammish repetition")
hd = h.hexdigest()

print(hd)

print(hashlib.algorithms)
#from 2.7.9
print(hashlib.algorithms_guaranteed)
print(hashlib.algorithms_available)
dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
xb = binascii.hexlify(dk)

print(xb)

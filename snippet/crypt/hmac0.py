import hmac

h0 = hmac.new("222")
hd0 = h0.digest()
print(hd0)
hd0 = h0.hexdigest()
print(hd0)


h1 = hmac.new("222")
hd1 = h1.hexdigest()


## start from 2.7.7
res = hmac.compare_digest("123","234")

print(res)

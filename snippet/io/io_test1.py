import io
import pickle
#StringIO
str1 = io.StringIO()
if str1.writable() :
    str1.write("1234")
else:
    print("not write")
print(str1)
print(str1.getvalue())
str1.close()


#BytesIO
byio = io.BytesIO()
print(byio.getvalue())
byio.write(b"123456")
bf = byio.getbuffer()
bf[0:2] = b"ab"
print(byio.getvalue())
del bf
byio.close()


#TextIO
print("---\n")
with open("xx","r") as fx:
    ll = fx.read(10)
    print(ll)

print("---\n")
with open("xx","r") as fx:
    for ll in fx:
        print(ll)
print("---\n")
done =0
with open("xx","r") as fx:
    while not done:
        ll = fx.readline()
        if ll == '':
            done =1
        else:
            print(ll)


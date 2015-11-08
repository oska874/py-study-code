import io

if __name__ == "__main__":
    str0 = io.StringIO()
    str0.write(u"abcde\n")
    print(str0.getvalue())

    byt0 = io.BytesIO()
    byt0.write("abcde\n".encode('ascii'))
    print(byt0.getvalue())


import StringIO

output = StringIO.StringIO()
output.write('First line.\n')
print >>output, 'Second line.'

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()
print(contents)

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()

import sqlite3

dbName = "/tmp/test.db"#":memory:"
conn = sqlite3.connect(dbName)

c = conn.cursor()

# Create table
c.execute('CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2016-01-25','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

conn = sqlite3.connect(dbName)
c = conn.cursor()

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2016-01-26', 'BUY', 'IBM', 1000, 45.00),
            ('2016-01-26', 'BUY', 'MSFT', 1000, 72.00),
            ('2016-01-26', 'SELL', 'IBM', 500, 53.00),
                                              ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

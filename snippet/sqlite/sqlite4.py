import sqlite3

class MySum1:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

if __name__ == "__main__":
    dbName = ":memory:"
    con = sqlite3.connect(dbName)

    con.create_aggregate("mysum", 1, MySum1)
    cur = con.cursor()
    cur.execute("create table test(i)")
    cur.execute("insert into test(i) values (1)")
    cur.execute("insert into test(i) values (2)")
    cur.execute("select mysum(i) from test")
    print(cur.fetchone()[0])
    cur.execute("select * from test")
    print(cur.fetchone()[0])
    print(cur.fetchone()[0])


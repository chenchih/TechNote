from mydb import MyDB
conn =None
cur = None
def setup_module():
    global conn
    global cur
    db = MyDB()
    conn=db.connect("server")
    cur=conn.cursor()

def teardown_module():
    cur.close()
    conn.close()

def test_john_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_ted_id(cur):
    db = MyDB()
    conn=db.connect("server")
    cur=conn.cursor()
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 456

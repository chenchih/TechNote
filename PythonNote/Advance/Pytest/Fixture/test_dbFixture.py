from mydb import MyDB
import pytest

@pytest.fixture(scope="module")
def setup():
    print("Setting Up!!!")
    db = MyDB()
    conn=db.connect("server")
    curs=conn.cursor()
    # return curs
    yield curs
    curs.close
    conn.close
    print("closing DB")


def test_john_id(setup):
    id = setup.execute("select id from employee_db where name=John")
    assert id == 123

def test_ted_id(setup):
    id = setup.execute("select id from employee_db where name=Tom")
    assert id == 456


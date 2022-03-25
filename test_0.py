import app
 
def test_add():
    output = app.add(1,2)
    assert output == 3
 
def test_subtract():
    output = app.subtract(5,2)
    assert output == 3
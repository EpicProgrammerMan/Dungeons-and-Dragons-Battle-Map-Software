# Simple example pytest script
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

from models import user_records
def test_1():
    for user in user_records:
        # Goes through all users and checks to see if any variables are None
        print(user.id)
        assert(user.id!=None)
def test2():
    for user in user_records:
        print(user.first_name)
        assert(user.first_name!='')
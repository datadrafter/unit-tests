"""
This is the following example of pytest assertions
This testing module helps write tests for complex methods and libraries

pip install -U pytest
pytest --version
import pytest

pytest -q basic_pytest.py
pytest -quiet basic_pytest.py
this quiet mode is to get less details while running

"""
import pytest

def inc(x):
    return x + 1

class TestClass:
    def test_answer():
        assert inc(3) == 4


# Using markers in pytest so marker test functions can be grouped and ran together
# Specify marker before each test
# @pytest.mark.any_name_for_grouping
# @pytest.mark.one and to run this use "pytest -m one"

"""
@pytest.mark.one
def test_answer():
    assert inc(3) == 4

in terminal: pytest -m one
"""

class TestClass():
    def test_one(self):
        x = "test"
        assert 't' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "hello")

#fixture in pytest
#whenever we want to run a block of code before running tests we use fixtures
@pytest.fixture
def numbers():
    a = 10
    b = 5
    c = 15

    return [a,b,c]

def test_method1(numbers):
    x = 15
    assert number[0] == x

def test_method2(numbers):
    y = 20
    assert number[1] == y

def test_method3(numbers):
    z = 25
    assert number[0] == z

#parameterize a test to run multiple arguments in a test

@pytest.mark.parametrize("x,y,z", [(10,20,40), (100,200,400)])
def test_method(x,y,z):
    assert x*y == z

# "@pytest.mark.skip" to skip any test while running

def test_method1(numbers):
    x = 10
    assert numbers[0] == x

@pytest.mark.skip
def test_method2(numbers):
    pass

@pytest.mark.skip
def test_method3(numbers):
    pass

#similarly use @pytest.mark.xfail to tell that we know the test will fail it shows xpass



# testing an API
import requests
import json

def main_url():
    return "https://reqres.in"

def test_valid_login():
    url = main_url + "/api/login"
    data = {'email': 'abc@xyz.com', 'password': 'qwerty'}
    response = requests.get(url, data=data)
    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == "QEFJ349Ddjh302v!"


# till here you are through with the pytest basics but below are some more data related to this module

""" 
This is how pytest raises works

def myfunc():
    raise ValueError("Exception 123 raised")

def test_myfunc():
    with pytest.raises(ValueError, match=r.*123.*)

"""

#sometimes we know a fixture that all our test will depend on so we can use autouse=True her

@pytest.fixture
def first_entry():
    return a

@pytest.fixture 
def order(first_entry):
    return []

@pytest.fixture(autouse=True)
def append_first(order,first_entry):
    return order.append(first_entry)

#fixture requiring netwrk access depend on connectivity

import smtplib

@pytest.fixture(scope="module",autouse=True)
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=580)

# monkey patch/ mock modules and environments
"""This helps you to safely set/delete an attribute, dictionary item or environment variable 
or modify sys.path for importing

monkeypatch.setattr(obj, name, value, raising=True) and monkeypatch.delattr(obj, name, raising=True):
Modifying the behaviour of a function or the property of a class for a test


monkeypatch.setitem(mapping, name, value) and monkeypatch.delitem(obj, name, raising=True):
Modify the values of dictionaries

monkeypatch.setenv(name, value, prepend=None) and monkeypatch.delenv(name, raising=True):
Modifying environment variables for a test

monkeypatch.syspath_prepend(path) and monkeypatch.chdir(path):
to Modify sys.path

def getssh():
    return Path.home()/ ".ssh"

def test_getssh(monkeypatch):
    def mockreturn():
        return Path("/abc")

    monkeypatch.setattr(Path, "home", mockreturn)
    x = getssh()
    assert x == Path("/abc/.ssh")

monkeypatch.context():
to apply patches only in a specific scope

"""

# pytest also integrates with doctest, unittest and nose
# we can log the pytest logs use ".ini" and log file path for reference use this link https://docs.pytest.org/en/7.2.x/how-to/logging.html
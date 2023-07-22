import pytest
import importlib

hello = importlib.import_module("001_hello").hello

def test_hello():
    assert hello("David")=="hello... , David"
    
def test_default():
    assert hello()=="hello... , world"
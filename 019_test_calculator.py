import pytest
import importlib
# calculator_module = importlib.import_module("003_calculator")

# square = calculator_module.square
square = importlib.import_module("003_calculator").square

def test_positive():
    assert square(2)==4
    assert square(3)==9
   
def test_negaitive():
    assert square(-2)==4
    assert square(-3)==9
    
def test_zero():
    assert square(0)==0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

    
# def test_square():
#     try:
#         assert square(2)==4
#     except AssertionError:
#         print("2 squared was not 4")   

#     try:
#         assert square(3)==9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:
#         assert square(-2)==4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3)==9
#     except AssertionError:
#         print("-3 squared was not 9")      
#     try:
#         assert square(0)==0
#     except AssertionError:
#         print("0 squared was not 0")
    

# def main():
#     test_square()

# if __name__== "__main__":
#     main()
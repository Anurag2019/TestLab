import pytest # type: ignore
from operations import add,subtract,mul,power,larger,smaller,equal,number
import warnings
warnings.filterwarnings("ignore")
@pytest.mark.arithematic
def test_add():
    assert add(6,8)==14
    assert add(3,5)==8
@pytest.mark.arithematic
def test_subtract():
    assert subtract(7,9)==2
    assert subtract(10,6)==4
@pytest.mark.arithematic
def test_mul():
    assert mul(4,5)==20
    assert mul(2,8)==16
@pytest.mark.arithematic
def test_power():
    assert power(3,2)==9
@pytest.mark.compare 
def test_larger():
    assert larger(4,9)==9

@pytest.mark.compare 
def test_smaller():
    assert smaller(3,8)==3
@pytest.mark.compare 
def test_equal():
    assert equal(7,7)==True
    assert equal(9,6)==False
@pytest.mark.boolean
def test_and():
    assert (20 and True)==True
    assert (40 and 60)==60
@pytest.mark.boolean
def test_or():
    assert (50 or 70)==50
    assert (False or 60)==60
    assert (True or 40)==True
def test_number():
    assert number(4,"even")==True
    assert number(3,"even")==False
    assert number(5,"odd")==True
    assert number(8,"odd")==False
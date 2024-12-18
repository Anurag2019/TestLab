from string_operations import exists,count,single_sentence,upper_name,count_words,is_pallindrome,string_type
import warnings
import pytest
warnings.filterwarnings("ignore")
@pytest.fixture
def sample_string():
    return "Hello"
def test_word_in_string():
    assert exists("hot","she is hot")==True
    assert exists("am","I am a student")==True
@pytest.mark.word
def test_count_word_in_string():
    assert count("good","He is good in studies and also a good human being")==2
    assert count("her","I love her and her family. I want to marry her")==3
def test_single_sentence():
    assert single_sentence("I am very lucky.I am an Indian.")==False
def test_upper_name(sample_string):
    assert upper_name("anurag")=="ANURAG"
    assert upper_name("mamta")=="MAMTA"
    assert upper_name(sample_string)=="HELLO"
@pytest.mark.word
def test_word_count():
    assert count_words("Beauty with brain")=="ODD"
def test_pallindrome(sample_string):
    assert is_pallindrome("level")==True
    assert not is_pallindrome(sample_string)
def test_string_type():
    assert string_type("abc","A")==True
    assert string_type("123","D")==True
    assert string_type("abc123","AN")==True

def test_sample_string(sample_string):
    assert sample_string=="Hello"
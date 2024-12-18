def exists(word,string):
    return True if word in string else False
def count(word,string):
    return string.count(word)
def single_sentence(string):
    l=list(string.split("."))
    l.pop()
    return True if len(l)==1 else False
def upper_name(name):
    return name.upper()
def count_words(sentence):
    words_list=sentence.split(" ")
    return "EVEN" if len(words_list) % 2==0 else "ODD"
def is_pallindrome(string):
    return True if string==string[::-1] else False
def string_type(string,type_code):
       if string.isdigit():
           type="D"
       elif string.isalpha():
           type="A"
       else:
           type="AN"
       if type.lower()==type_code.lower():
           return True
       else:
           return False
        
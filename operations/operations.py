def add(x,y):
    return x+y
def mul(x,y):
    return x*y
def subtract(x,y):
    return x-y if x>y else y-x
def power(n1,n2):
    return pow(n1,n2)
def larger(n1,n2):
    return n1 if n1>n2 else n2
def smaller(n1,n2):
    return n1 if n1<n2 else n2
def equal(n1,n2):
    return True if n1==n2 else False
def number(num,s):
    status="Even" if num%2==0 else "Odd"
    return True if status.lower()==s.lower() else False
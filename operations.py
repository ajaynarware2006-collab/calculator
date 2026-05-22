from utils import get_number

def add(a,b):
    return a+b
     
def subtact(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        x=a/b
        return x
    except ZeroDivisionError:
        return ("Second number should not equle to Zero")

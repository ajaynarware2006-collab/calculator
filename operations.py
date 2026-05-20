from utils import get_number

def add():
   sum=0
   while True:
       value=get_number()
       if value =="=":
           return sum
       else:
            try:
                int_value=int(value)
                sum+=int_value
            except ValueError:
                None
     
def subtact(a,b):
    result=0
    while True:
        value=get_number()
        if value =="=":
            return result
        else:
            try:
                int_value=int(value)
                result-=int_value
            except ValueError:
                None

def multiply(a,b):
    result=0
    while True:
        value=get_number()
        if value =="=":
           return result
        else:
            try:
                int_value=int(value)
                result*=int_value
            except ValueError:
                None

def divide(a,b):
    try:
        result=0
        while True:
            value=get_number()
            if value =="=":
               return result
            else:
                try:
                    int_value=int(value)
                    result/=int_value
                except ValueError:
                    None
    except ZeroDivisionError:
        return ("Zero division Erorr")

"""Basic math operations."""


def add(a, b):
    if(a.isnumeric() & b.isnumeric()):
     a=float(a)
     b =float(b)
     operation =  a + b
     return   operation

def sub(a, b):
    if(a.isnumeric() & b.isnumeric()):
     a= float(a)
     b = float(b)
     operation = a - b
    return  operation

def mult(a, b):
   if(a.isnumeric() & b.isnumeric()):
    a= float(a)
    b = float(b)
    operation =  a  * b
    return  operation

def div(a, b):
    if(a.isnumeric() & b.isnumeric()):
     a= float(a)
     b = float(b)
     operation  =  a/b
    return   operation
    
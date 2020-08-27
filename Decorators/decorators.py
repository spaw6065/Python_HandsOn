)
def logger(func):
    def inner(*args,**kwargs):
        print(f"Arguments are {args} and {kwargs}")
        return func(*args,**kwargs)
    return inner

@logger
def add(x,y=0):
    return x+y
@logger
def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y=1):
    return x/y



print(add(2,5))
print(sub(5,2))
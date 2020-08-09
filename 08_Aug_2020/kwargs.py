def add(*args):
    print("args",*args)

add(2,3,4,5)

def myfunc(**kwargs):
    print("kwargs",**kwargs)
    for key,value in kwargs.items():
        print(f"for id {key} value is {value}")

myfunc(a=10,b=20,c=30)
from functools import wraps


def decorate(func):
    @wraps(func)
    def wrapper(args, **kwargs):
        print("Start ...")
        func(args, **kwargs)
        print("End ...")
    return wrapper

@decorate
def add(x):
    print(x + x)
    print("Called")

# add(2)
# print(help(add))
# print(add.__name__)



# nested decortors
def repeat(no_of_times):
    def decorator_repeat(func):
        @wraps(func)
        def actual_repeat(args, **kwargs):
            for _ in range(no_of_times):
                result = func(args, **kwargs)
            return result
        return actual_repeat
    return decorator_repeat 

@decorate
@repeat(no_of_times=6)
def greet(name):
    print(f"Hi {name}")
    
# greet("jay")


# class based decoratrs 
class Person:
    def __init__(self, func):
        self.func = func
        self.num_of_calls = 0
        
    def __call__(self, *args, **kwargs):
        self.num_of_calls += 1
        # print("Called", self.num_of_calls)
        print(*args, "ARGS")
        self.func(*args, **kwargs)


@Person
def isMe(x,*args):
    pass
    # print("This is me calling")
    
for i in range(10):
    isMe(3,2,3,4)
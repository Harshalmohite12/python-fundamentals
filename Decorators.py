# def main(func):
#     def wrapper(*args, **kwargs):
#         print("Hello")
#         return func(*args, **kwargs)
#     return wrapper

# @main
# def add(a, b):
#     print(a+b)
    

# add(4 ,67)


# def log(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with {args} {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @log
# def multiply(a, b):
#     return a * b

# print(multiply(3, 4))

# def decorator(func):
#     count =0
#     def wrapper():
#         nonlocal count
#         func()
#         count += 1
#         print(f"This functon {func.__name__} is called {count} times.")
#     return wrapper

# @decorator
# def say_hello():
#     print("Hello Wolrd!")
    
# say_hello()
# say_hello()
# say_hello()
# say_hello()


# x = 100   # global

# def outer():
#     count = 0   # enclosing (outer function variable)

#     def middle():
#         nonlocal count   # refers to 'count' in outer()
#         count += 1
#         print("Middle:", count)

#         def inner():
#             nonlocal count   # still refers to 'count' in outer()
#             count += 1
#             print("Inner:", count)

#         inner()

#     middle()
#     print("Outer:", count)

# outer()


# def show_name(func):
#     def wrapper(*args):
#         print(f"Calling function: {func.__name__}")
#         return func(*args)
#     return wrapper



# @show_name
# def add(a, b):
#     return a + b

# @show_name
# def greet(name):
#     print(f"Hello {name}!")
    
# print(add(3, 5))
# greet("Harshal")

# def safe_divide(func):
#     def wrapper(*args, **kwargs):
#         a = [*args]
#         for i in range (0, len(a)):
#             if a[i] == 0:
#                 return "Cannot divide by zero"
#         return func(*args, **kwargs)
#     return wrapper

# @safe_divide
# def divide(a, b):
#     ressult =  a / b
#     return ressult

# print(divide(10, 2))
# print(divide(5, 0))

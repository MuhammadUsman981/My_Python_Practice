# let's Define Function
def greet_user():
    print("Hello User!")
#greet_user()

def aoa(name):
    print(f"Assalam o alikom!, {name},How are you")
#aoa("Muhmmad Usman")

def aoa(name="Good User"):
    print(f"Assalam o alikom!, {name},How are you")
# aoa()
# Return value

def square(number):
    return number * number

# print(square(9))

def square(number):
    return number * number
result = square(8)
#print(result)


# Recursion
def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
   # print(factorial(4))
    
# Lambda Function

x = lambda a : a * 10
# print(x(20))

def x(a):
    return a/2
# print(x(10))

x = lambda a: a/3
# print(x(9))

def x(a,b):
    return a+b
# print(x(10,20))

x = lambda a , b : a + b
# print(x (10,20))


def greet():
    print("Hello User!")

greet()

def add(a,b):
    return a + b

print(add(10,20))

def greet_user(name= "Good user"):     # Good User is only if some one do not provide there name 
    print(f"Hello!,{name}, How are you doing") 
greet_user("USMAN")


def calculate(a,b):
    return a+b
print(calculate(7,9))


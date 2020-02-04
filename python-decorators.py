'''
Created on Aug 2, 2013

@author: tunatore
'''

#decorators are similar to Aspect Oriented Programming in JAVA
#They have the ability to run after or before any function
#decorators are applied with @character
#you can use built-in decorators such as @staticmethod

class Hello():
    @staticmethod
    def f():
        return "Hello"

print (Hello.f())

class HelloInstance():
    def f(self):
        return "Hello from Instance"

#the following won't work
#print (HelloInstance.f())
#you should try

hwi = HelloInstance()
print (hwi.f())


class User:
    """User class"""
    id = 1234567890
    name = "tuna"

#CHANINED decorators
def trace(f):
    def newFunc(): #any def method name is allowed such as new,newFunc or wrapper ..
        print ("tracing..")
        f()
    return newFunc

def storelastlogin(f):
    def newFunc():
        print ("storing..")
        f()
    return newFunc

@trace
@storelastlogin
def login():
    print ("user ID: " + str(User().id) + " name: " + User().name)

login()

def beforeAndAfter(f):
    def newFunc():
        print ("before.. is called")
        f()
        print ("after.. is called")
    return newFunc

@beforeAndAfter
def loginSecond():
    pass #do nothing

loginSecond()

#CHANGING LOGIC
def changeFunctionLogic(f):
    def newFunc(*args): #any def method name is allowed such as new,newFunc or wrapper ..
        print ("changing output by multiplying function itself")
        return f(*args) * f(*args)
    return newFunc

@changeFunctionLogic
def multiplyNumbers(arg1,arg2):
    return arg1 * arg2

print ("Result (2*2) * (2*2) =", multiplyNumbers(2, 2))
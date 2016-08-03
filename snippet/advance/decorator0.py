# -*- coding: utf-8 -*-
#copyright:http://coolshell.cn/articles/11265.html

def hello(fn):
    def wrapper():
    	print "hello, %s" % fn.__name__
        fn()
        print "goodby, %s" % fn.__name__
	print "11hello, %s" % fn.__name__
    return wrapper
 
@hello
def foo():
    print "a i am foo"
 
print("test 0")
foo()
print("test 0.1")

#@decorator
#def func():
#    pass
#其解释器会解释成下面这样的语句：
#func = decorator(func)

def fuck(fn):
    print "fuck %s!" % fn.__name__[::-1].upper()
    fn()
 
@fuck
def wfg():
	print("will not run this")

print("test 1")
wfg

def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) if "css_class" in kwds else ""
        def wrapped(*args, **kwds):
            return "<"+tag+css_class+">" + fn(*args, **kwds) + "</"+tag+">"
        return wrapped
    return real_decorator
 
@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"
 
print("test 2")
print hello()

#class decorator
class myDecorator(object):
 
    def __init__(self, fn):
        print "inside myDecorator.__init__()"
        self.fn = fn
 
    def __call__(self):
        self.fn()
        print "inside myDecorator.__call__()"

    def  test():
    	print("11111")
 
@myDecorator
def aFunction():
    print "inside aFunction()"
 
print "Finished decorating aFunction()"
 
aFunction()


#用Decorator设置函数的调用参数
#第一种，通过 **kwargs，这种方法decorator会在kwargs中注入参数。
def decorate_A(function):
    def wrap_function(*args, **kwargs):
        kwargs['str'] = 'Hello!'
        return function(*args, **kwargs)
    return wrap_function
 
@decorate_A
def print_message_A(*args, **kwargs):
    print(kwargs['str'])
 
print_message_A()

#第二种，约定好参数，直接修改参数
def decorate_B(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        return function(str, *args, **kwargs)
    return wrap_function
 
@decorate_B
def print_message_B(str, *args, **kwargs):
    print(str)
 
print_message_B()


#第三种，通过 *args 注入
def decorate_C(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        #args.insert(1, str)
        args = args +(str,)
        return function(*args, **kwargs)
    return wrap_function
 
class Printer:
    @decorate_C
    def print_message(self, str, *args, **kwargs):
        print(str)
 
p = Printer()
p.print_message()


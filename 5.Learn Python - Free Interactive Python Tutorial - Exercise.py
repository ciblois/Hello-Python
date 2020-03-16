Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = ("John", "Doe", 53.44)
>>> format_string = "Hello"
>>> print(format_string "%s %s. Your current balance is $%f" % (data[0],data[1],data[2]))
SyntaxError: invalid syntax
>>> print(format_string + "%s %s. Your current balance is $%f" % (data[0],data[1],data[2]))
HelloJohn Doe. Your current balance is $53.440000
>>> print(format_string + " %s %s. Your current balance is $%f" % (data[0],data[1],data[2]))
Hello John Doe. Your current balance is $53.440000
>>> print(format_string + " %s %s. Your current balance is $%s" % (data[0],data[1],data[2]))
Hello John Doe. Your current balance is $53.44
>>> 

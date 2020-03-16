Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #EXERCISE 2
>>> mystring = "hello"
>>> myfloat = 10.0
>>> myint = 20
>>> # testing code
>>> if mystring == "hello":
	print("String: %s" % mystring)

	
String: hello
>>> if isinstance(myfloat, float) and myfloat == 10.0:
	    print("Float: %f" % myfloat)

	    
Float: 10.000000
>>> if isinstance(myint, int) and myint == 20:
	    print("Integer: %d" % myint)

	    
Integer: 20
>>> holds_types = [type(mystring), type(myfloat), type(myint)]
>>> print(str(holds_types))
[<class 'str'>, <class 'float'>, <class 'int'>]
>>> 

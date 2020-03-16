Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #EXERCISE 4
>>> x = object()
>>> y = object()
>>> # TODO: change this code
>>> x_list = [x] * 10
>>> y_list = [y] * 10
>>> big_list = x_list + y_list
>>> print("x_list contains %d objects" % len(x_list))
x_list contains 10 objects
>>> print("y_list contains %d objects" % len(y_list))
y_list contains 10 objects
>>> print("big_list contains %d objects" % len(big_list))
big_list contains 20 objects
>>> # testing code
>>> if x_list.count(x) == 10 and y_list.count(y) == 10:
	    print("Almost there...")

	    
Almost there...
>>> if big_list.count(x) == 10 and big_list.count(y) == 10:
	    print("Great!")

	    
Great!
>>> 

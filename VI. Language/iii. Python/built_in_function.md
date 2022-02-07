# :books: Built-in Function | [Document Python 3.7.9](https://docs.python.org/3.7/library/functions.html)
`This page is from 'iii. Python/readme.md'`

### **abs**(*x*)
Return the absolute value of a number. The argument may be an integer or a floating point number. If the arguemtn is a complex number, its magnitude is returned.

### **all**(*iterable*)
Return `True` if all elements of the *iterable* are true (or if the iterable is empty).

### **any**(*iterable*)
Return `True` if any element of the *iterable* is true. If the iterable is empty, return `False`.

### **ascii**(*object*)
As [repr()](), return a string containing a printable representation of an object, but escape the non-ASCII characters in the string returned by [repr()]() using `\x`, `\u` or `\U` escapes. This generates a string similar to that returned by [repr()]() in Python 2.

### **bin**(*x*)
Convert an integer number to a binary string prefixed with "0b". The result is a valid Python expression. If *x* is not a Python [int]() object, it has to define an [__index__()]() method that returns an integer.

### *class* **bool**([*x*])
Return a Boolean value, i.e. one of `True` or `False`. *x* is converted using the standard [truth testing procedure](). If *x* is false or omitted, this returns `False`; otherwise it returns `True`. The bool class is a subclass of [int]() (see [Numeric Types - int, float, complex]()). It cannot be subclassed futher. Its only instances are `Flase` and `True` (see [Boolean Values]().

### **breakpoint**(* *args* , ** *kws*)
This function drops you into the debugger at the call site. Specifically, it calls [sys.breakpointhook()](), passing `args` and `kws` straight through. By default, `sys.breakpointhook()` calls [pdb.set_trace()]() expecting no arguments. In this case, it is purely a convenience function so you don't have to explicitly import [pdb]() or type as much code to enter the debugger. However, [sys.breakpointhook()]() can be set to some other function and [breakpoint()]() will automatically call that, allowing you to drop into the debugger of choice.

### *class* **bytearray**([*source*[, *encoding*[, *errors*]]])
Return a new array of bytes. The [bytearray]() class is a mutable sequence of integers in the range `0 <= x < 256`. It has most of the usual methods of mutable sequences, described in [Mutable Sequence Types](), as well as most methods that the [bytes]() type has, see [Bytes and Bytearray Operations]().

### *class* **bytes**([*source*[, *encoding*[, *errors*]]])
Return a new "bytes" object, which is an immutable sequence of integers in the range `0 <= x < 256`. [bytes]() is an immutable version of [bytearray]() - it has the same non-mutating methods and the same indexing and slicing behavior.

### **callable**(*object*)
Return [True]() if the *object* argument appears callable, [False]() if not. If this returns `True`, it is still possible that a call fails, but if it is `False`, calling *object* will never succeed. Note that classes are callable (calling a class returns a new instance); instances are callable if their class has a [__call__()]() method.

### **chr**(*i*)

### **@classmethod**

### **compile**(*source, filename, mode, flags=0, dont_inherit=False, optimize=-1*)

### *class* **complex**([*real*[, *imag*]])

### **delattr**(*object*, *name*)

### *class* **dict**(***kwarg*)

### *class* **dict**(*mapping*, **kwarg)

### *class* **dict**(*iterable*, **kwarg)

### **dir**([*object*])

### **divmod**(*a*, *b*)
Take tow (non complex) numbers as arguments and return a pair of numbers consisting of their quotient and remainder when using integer division. With mixed oprand types, the rules for binary arithmetic operators apply. For integers, the result is the same as `( a // b, a % b)`. For floating point numbers the result is `(q, a % b)`, where *q* is usually `math.floor(a / b)` but may be 1 less than that. In any case `q * b + a % b` is very close to *a*, if `a % b` is non-zero it has the same sign as *b*, and `0 <= abs(a % b) < abs(b)`.

### **enumerate**(*iterable*, *start=0*)
Return as enumerate object. *iteralbe* must be a sequence, an [iterator], or some other object which supports iteration. The [__next__()]() method of the iterator returned by [enumerate()] returns a tuple containing a count (from *start* which defaults to 0) and the values obtained from iterating over *iterable*.

### **eval**(*expression*[, *globals*[, *locals*]])

### **exec**(*object*[, *globals*[, *locals*]])

### **filter**(*function*, *iterable*)

### *class* **float**([*x*])

### **format**(*value*[, *format_spec*])
Convert a *value* to a "formatted" representation, as controlled by *format_spec*. The interpretation ofr *format_spec* will depend on the type of the *value* argument, however there is a standard formatting syntax that is used by most built-in types: [Format Specification Mini-Language]().

### *class* **frozenset**([*iterable*])
Return a new [frozenset]() object, optionally with elements taken from *iterable*. `frozenset` is a built-in class.

### **getattr**(*object*, *name*[, *default*])
Return the value of the named attributed of *object*. *name* must be a string. If the string is the name of one of the object's attributes, the result is the value of that attribute. For example, `getattr(x, 'foobar')` is equivalent to `x.foobar`. If the named attributes does not exist, *default* is returned if provided, otherwise [AttributeError]() is raised.

### **globals**()
Return a dictionary representing the current global symbol table. This is always the dictionary of the current module (inside a function or method, this is the module where it is defined, not the module from which it is called).

### **hasattr**(*object*, *name*)
The arguments are an object and a string. The result is `True` if the string is the name of one of the object's attributes. `False` if not. (This is implemented by calling `getattr(object, name)` and seeing whether it raises an [AttributeError]() or not).

### **hash**(*object*)

### **help**([*object*])

### **hex**(*x*)

### **id**(*object*)
Return object's address in CPython.

### **input**([*prompt*])

### *class* **int**([*x*])

### *class* **int**(*x*, *base=10*)

### **isinstance**(*object*, *classinfo*)
Return `True` if the object argument is an instance of the classinfo argument, or of a (direct, indirect or [virtual]()) subclass thereof. If *object* is not an object of the given type, the function always returns `False`. If *classinfo* is a tuple of type objects (or recursively, other such tuples), return `True` if *object* is an instance of any of the types. If *classinfo* is not a type or tuple of types and such tuples, a [TypeError]() exception is raised.

### **issubclass**(*class*, *classinfo*)

### **iter**(*object*[, *sentinel*])

### **len**(*s*)

### *class* **list**([*iterable*])

### **locals**()

### **map**(*funtion*, *iterable*, *...*)

### **max**(*iterable*, *[, *key*, *default*])

### **max**(*arg1*, *arg2*, * *args*[, *key*])

### **min**(*iterable*, *[, *key*, *default*])

### **min**(*arg1*, *arg2*, * *args*[, *key*])

### **next**(*iterator*[, *default*])

### *class* **object**

### **oct**(*x*)

### **open**(*file*, *mode='r'*, *buffering=-1*, *encoding=None*, *errors=None*, *newline=None*, *closefd=True*, *opener=None*)

### **ord**(*c*)

### **pow**(*x*, *y*[, *z*])

### **print**(* *objects*, *sep=''*, *end='\n'*, *file=sys.stdout*, *flush=False*)

### *class* **property**(*fget=None*, *fset=None*, *fdel=None*, *doc=None*)

### *class* **range**(*stop*)

### *class* **range**(*start*, *stop*[, *step*])

### **repr**(*object*)
Return a string containing a printable representation of an object. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a __repr__() method.

### **reversed**(*seq*)
Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).

### **round**(*number*[, *ndigits*])

### *class* **set**([*iterable*])

### **setattr**(*object*, *name*, *value*)

### *class* **slice**(*stop*)

### *class* **slice**(*start*, *stop*[, *step*])

### **sorted**(*iterable*, *, *key=None*, *reverse=False*)

### **@staticmethod**
Transform a method into a static method.

### *class* **str**(*object=''*)

### *class* **str**(*object=b''*, *encoding='utf-8'*, *errors='strict'*)

### **sum**(*iterable*[, *start*])

### **super**(*type*[, *object-or-type*]])

### *class* **tuple**([iterable*])

### *class* **type**(*object*)

### *class* **type**(*name*, *bases*, *dict*)

### **vars**([*object*])

### **zip**(* *iterables*)

## __import__(*name*, *globals=None*, *locals=None*, *fromlist=()*, *level=0*)

# C++
This page is about C and C++.

## Data Type
|Type Name|Byte|Nickname|Value Range|
|:-------:|:--:|:------:|:---------:|
|int|4|signed|-2,147,483,648 to 2,147,483,647|
|unsigned int|4|unsigned|0 to 4,294,967,295|
|bool|1|none|false or true|
|char|1|none|-128 to 127|
|signed char|1|none|-128 to 127|
|unsigned char|1|none|0 to 255|
|short|2|short int, signed short int|-32,768 to 32,767|
|unsigned short|2|unsigned short int|0 to 65,535|
|long|4|long int, signed long int|-2,147,483,648 to 2,147,483,647|
|unsigned long|4|unsigned long int|0 to 4,294,967,295|
|long long|8|none|-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807|
|unsigned long long|8|none|0 to 18,446,744,073,709,551,615|
|enum|varies|none|varies|
|float|4|none|3.4E +/- 38 (7 digits)|
|double|8|none|1.7E +/- 308 (15 digits)|
|long double|8|none|1.7E +/- 308 (15 digits)|

## untitled

### Ternary Operator
`Conditional statement ? return value 1 : return value 2`

If the conditional statment is true, return value 1 if it is false, return value 2.

### `friend` Class
It can access to `private` and `protected member` to other `friend class`.

### `friend` Function
Same as `friend class`, it gives other to access `private` and `protected member` with function unit not as class unit.

### Static Variable (`static` as local variable)
It can use as global variable in corresponding source code, and keep after scope is ended, plus it only initialized for once and keeps until program end. It has same scope as local variable but alive until program end as global variable. 

### `virtual`
It used to declare function virtually in parent class, and it make child class declare in real. It used to manage modules as component, as modules have one same parent and make class as themselves with specify along their property.

### Template
It codes only `.h`s not `.cc`s.

### Smart pointer
C++ provides smart pointer to guarantee program's secure with memory leak. It is class template works as pointer, it releases memory automatically when useless. There was `auto_ptr` before C++11, and after C++11, there are `unique_ptr`, `shared_ptr`, and `weak_ptr`.

### `boost::scoped_ptr`
One of smart pointer, but restrained. It is same as `auto_ptr` without copying function.

### `override`
This keyword used at child class's virtual function, as `virtual` keyword is used front of function and at parent class, but `override` keyword is used end of function and at child class. Plus, `final` keyword is used at the last child class, and it means there will be no more virtual function over riding.

### `typedef`
It can make nickname of type. For example, `typedef double d` means `d` is nickname of type `double`. It can't define new type.

### sstream
#### istringstream
It used to parse(input) string.

#### ostringstream
It used to save(output) string.

#### stringstream
It used to modifie data of string.

### C Style Cast
`(type-id)(e-pression)`

It can convert(cast) A type to B type, it can convert(cast) any type to any type.

### C++ Style Cast
`<type-id>(e-pression)`

It can convert(cast) A type to B type, it has to use right cast.

#### `const_cast`
It removes or grant constness to expression. It rarley used to grant constness to expression.

#### `reinterpret_cast`
It can convert/cast any type of pointer to any type of pointer, for example, pointer to integer or integer to pointer, everything is possible.

#### `static_cast`
It is basic cast as having same meaning and same ability to convert/cast as C style cast.
It has limit as can't convert/cast struct type to int/double or float to pointer, and can't remove constness.
It's name is because it checks its' type at moment of compile not at run-time.

#### `dynamic_cast`
It is casting operator used to traverse inheritance hierarchy dynamically at run time or when downcasting.
It casts pointer or reference's base class instance to derived class or sibling class type.
It can't be casted between nonpolymorphic objects, and a compliation error occurs when attempting.

### Static Versus Dynamic Binding

### Forward Declarartions and Definitions

### Anonymous Namespace

### Extern Versus Static Versus Class Static

### Singleton

#### Reference
- Ternary Operator, http://tcpschool.com/cpp/cpp_operator_etc, 2020-06-08-Mon.
- Friend Class, Friend Function, https://yeolco.tistory.com/116, 2020-06-11-Thu.
- Static Variable, https://boycoding.tistory.com/169, 2020-06-11-Thu.
- Virtual, https://unikys.tistory.com/355, 2020-06-11-Thu.
- Smart Pointer, http://tcpschool.com/cpp/cpp_template_smartPointer, 2020-06-11-Thu.
- boost::scoped_ptr, https://yesarang.tistory.com/53, 2020-06-11-Thu.
- Multi Inheritance, https://m.blog.naver.com/PostView.nhn?blogId=kks227&logNo=60207057116&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-06-11-Thu.
- Override, https://blankspace-dev.tistory.com/412, 2020-06-11-Thu.
- Typedef, https://boycoding.tistory.com/182, 2020-06-11-Thu.
- sstream, https://doitnow-man.tistory.com/207, 2020-06-18-Thu.
- cast, http://egloos.zum.com/sweeper/v/1907485, 2020-06-18-Thu.
- Data Type, https://offbyone.tistory.com/115, 2020-06-18-Fri.

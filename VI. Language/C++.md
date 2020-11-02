# C++ | [cpp reference](https://en.cppreference.com/w/) | [Wiki (KR-KO)](https://ko.wikipedia.org/wiki/C%2B%2B)
```
This page is from the "Language" page.
```
C++는 AT&T 벨 연구소의 비야네 스트롭스트룹이 C언어 기반으로 1983년 발표하여 발전한 프로그래밍 언어이다.

- Tool: Visual Studio (by Microsoft), CLion (by JetBrains), CppCode (by Apple)

### Data Type
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

### Standard Template Library(STL)
Library that provides data structure and algorithm as template

#### Algorithm
Is is a function template that provides a generalized way to solve sorts, deletes, searches, operations, etc.

#### Allocator
It is a class object that encapsulates a container's memory allocation policy. Every container has its own allocator.

#### Container
It also called an object or data structure that stores objects. It is implemented as a class template.

##### Associative Container
###### array
###### vector
###### list
###### deque
##### Sequence Container
###### set
###### multiset
###### map
###### multimap
#### Container Adaptor
It changes the component's interface to a component with a new interface.

##### stack
##### queue
##### Priority_queue
#### Function Object
It is an object that behaves like a function, with the operator() operator overloaded. Client policy is reflected in containers and algorithms.

#### Iterator
It is a function similar to a pointer that points to an element in a container, accesses the element it points to, and points to the next element.

### untitled

#### Ternary Operator
`Conditional statement ? return value 1 : return value 2`

If the conditional statment is true, return value 1 if it is false, return value 2.

#### `friend` Class
It can access to `private` and `protected member` to other `friend class`.

#### `friend` Function
Same as `friend class`, it gives other to access `private` and `protected member` with function unit not as class unit.

#### Static Variable (`static` as local variable)
It can use as global variable in corresponding source code, and keep after scope is ended, plus it only initialized for once and keeps until program end. It has same scope as local variable but alive until program end as global variable. 

#### `virtual`
It used to declare function virtually in parent class, and it make child class declare in real. It used to manage modules as component, as modules have one same parent and make class as themselves with specify along their property.

#### Template
It codes only `.h`s not `.cc`s.

#### Smart pointer
C++ provides smart pointer to guarantee program's secure with memory leak. It is class template works as pointer, it releases memory automatically when useless. There was `auto_ptr` before C++11, and after C++11, there are `unique_ptr`, `shared_ptr`, and `weak_ptr`.

#### `boost::scoped_ptr`
One of smart pointer, but restrained. It is same as `auto_ptr` without copying function.

#### `override`
This keyword used at child class's virtual function, as `virtual` keyword is used front of function and at parent class, but `override` keyword is used end of function and at child class. Plus, `final` keyword is used at the last child class, and it means there will be no more virtual function over riding.

#### `typedef`
It can make nickname of type. For example, `typedef double d` means `d` is nickname of type `double`. It can't define new type.

#### sstream
##### istringstream
It used to parse(input) string.

##### ostringstream
It used to save(output) string.

##### stringstream
It used to modifie data of string.

#### C Style Cast
`(type-id)(e-pression)`

It can convert(cast) A type to B type, it can convert(cast) any type to any type.

#### C++ Style Cast
`<type-id>(e-pression)`

It can convert(cast) A type to B type, it has to use right cast.

##### `const_cast`
It removes or grant constness to expression. It rarley used to grant constness to expression.

##### `reinterpret_cast`
It can convert/cast any type of pointer to any type of pointer, for example, pointer to integer or integer to pointer, everything is possible.

##### `static_cast`
It is basic cast as having same meaning and same ability to convert/cast as C style cast.
It has limit as can't convert/cast struct type to int/double or float to pointer, and can't remove constness.
It's name is because it checks its' type at moment of compile not at run-time.

##### `dynamic_cast`
It is casting operator used to traverse inheritance hierarchy dynamically at run time or when downcasting.
It casts pointer or reference's base class instance to derived class or sibling class type.
It can't be casted between nonpolymorphic objects, and a compliation error occurs when attempting.

#### Call

##### Call by Value
값에 의한 호출을 통해 메모리 공간에서는 함수를 위한 별도의 임시 공간 stack frame이 생성되고, 함수 호출 시 전달되는 변수의 값을 복사해서 함수의 인자로 전달한다. 복사된 인자는 함수 안에서 지역적으로 사용되는 local value의 특성을 가진다. 따라서 함수 안에서 인자의 값이 변경되어도, 외부의 변수 값은 변경되지 않는다.

큰 구조체 또는 클래스를 함수에 전달할 때 값으로 전달하면 인수의 복사본을 함수 매개 변수로 만든다. 이 경우 복사하는데 큰 비용이 들어 성능이 저하될 수 있다. 그리고 값으로 인수를 전달할 경우 함수에서 호출자에게 값을 반환하는 유일한 방법은 함수의 반환 값을 사용하는 것이다. 이 방법도 좋지만, 함수에서 인수를 수정하는 것이 더 명확하고 효율적일 수 있다.

##### Call by Reference (Pass by Reference)

call by reference/pass by reference 참조로 전달하면 함수를 위한 별도의 임시 공간은 생성되지만, 함수 호출 시 인자로 전달되는 변수의 레퍼런스를 전달 받아 해당 변수를 가르키기 때문에 인자의 값이 변경되면 argument로 전달된 object의 값도 함께 변경된다.

#### Static

##### Static Member Variable
정적 멤버 변수는 클래스에는 속하지만 객체 별로 할당되지 않고 클래스의 모든 객체가 공유한다. 해당 클래스의 모든 객체에 대해 하나의 데이터만이 유지 관리된다. 선언은 클래스 영역에서 되지만, 정의는 파일 영역에서 수행된다. 이러한 정적 멤버 변수는 외부 연결을 가지므로, 여러 파일에서 접근할 수 있다.

정적 멤버 변수에도 클래스 멤버의 접근 제한 규칙이 적용되므로, 클래스의 멤버 함수나 프렌드만이 접근할 수 있다. 하지만 외부에서도 접근할 수 있게 하고 싶으면, public 영역에 선언하면 된다.

#### Static Member Function
정적 멤버 함수는 해당 클래스의 객체를 생성하지 않고도, 클래스 이름만으로 호출할 수 있다. 문법으로는 `object_name.member_function_name();`는 일반 멤버 함수의 호출이고, `class_name.member_function_name();`으로도 호출 가능하다. 정적 멤버 함수는 정적 멤버 변수를 선언하는 방법과 같이 static 키워드를 사용해서 선언한다. 특징으로는 객체를 생성하지 않고 클래스 이름만으로 호출 가능하며, 객체를 생성하지 않으므로 this 포인터를 가지지 않고, 특정 객체와 결합하지 않으므로 정적 멤버 변수만 사용 가능하다.

#### Const

##### Constant Member Variable
상수 멤버 변수란 한번 초기화하면, 그 값을 변경할 수 없는 멤버 변수이며 `const` 키워드를 사용한다. 문법으로는 `const type_name member_variable_name;`으로 쓴다.

##### Constant Member Function
상수 멤버 함수란 호출한 객체의 데이터를 변경할 수 없는 멤버 함수이며 함수의 원형 마지막에 `const` 키워드를 사용하여 선언한다. 호출한 객체의 데이터를 단순히 읽기만 하는 멤버 함수는 상수 멤버 함수로 정의하는 것이 정보 보호 측면에서 좋다. `function_name const;`

#### `->`
포인터 변수의 값을 참조하기 위한 연산자이다.

```
struct foo_struct
{
    char bar_arr[10];
    int bar_int = 10;
};

struct foo_struct *a
```
- O: `a->bar_arr`
- O: `a->bar_int`
- X: `a.bar_arr`
- X: `a.bar_int`

B는 포인터이므로 메모리에 주소만 가지고 있다. 따라서 `a.bar_arr`가 되지 않고 `a->bar_arr`가 된다.

#### #if #elif #else #endif
```
#if condition1
function1();

#elif condition2
function2();

#else
function3();

#endif
```

##### Static Versus Dynamic Binding

##### Forward Declarartions and Definitions

##### Anonymous Namespace

##### Extern Versus Static Versus Class Static

##### Singleton

### initialize function argument
- foo.h
```
void foo(int bar = 0);
```

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
- STL, https://blockdmask.tistory.com/67, 2020-06-18-Fri.
- STL, https://m.blog.naver.com/PostView.nhn?blogId=psd0217&logNo=220308769007&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-06-18-Fri.
- Call by Value, https://boycoding.tistory.com/217, 2020-06-25-Thu.
- Call by Reference, Call by Assignment, https://wayhome25.github.io/cs/2017/04/11/cs-13/, 2020-06-25-Thu.
- Static, Const, http://tcpschool.com/cpp/cpp_encapsulation_staticConst, 2020-06-25-Thu.
- ->, https://m.blog.naver.com/PostView.nhn?blogId=reverse_ing&logNo=60133603796&proxyReferer=https:%2F%2Fwww.google.com%2F, 2020-07-01-Wed.
- #if, #elif, #else, #endif, https://docs.microsoft.com/ko-kr/cpp/preprocessor/hash-if-hash-elif-hash-else-and-hash-endif-directives-c-cpp?view=vs-2019, 2020-07-13-Mon.
- C++ Wiki KR-KO, https://ko.wikipedia.org/wiki/C%2B%2B, 2020-11-02-Mon.

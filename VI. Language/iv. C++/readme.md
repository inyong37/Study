# *C++* | [Standard C++](https://isocpp.org/) | [cppreference](https://en.cppreference.com/w/) | [Wiki (KR)](https://ko.wikipedia.org/wiki/C%2B%2B)
```
This page is from the "Language" page.
```
C++는 AT&T 벨 연구소의 비야네 스트롭스트룹이 C언어 기반으로 1983년 발표하여 발전한 프로그래밍 언어이다.

- Tool: Visual Studio (by Microsoft), CLion (by JetBrains), CppCode (by Apple)

----------

## :books: Type | [cppreference](https://en.cppreference.com/w/cpp/language/types)
### Void Type
- Void
type with an empty set of values. It is an incomplete type that cannot be completed (consequently, objects of type void are disallowed). There are no arrays of void, nor references to void. However, pointers to void and functions returning type void (procedures in other languages) are permitted.

- std::nullptr_t

### Data Models

### Integer Types

### Boolean Type
- bool
Type, capable of holding one of the two values: true or false. The value of siezof(bool) is implementation defined and might differ from 1.

### Character Types
- signed char
Types for signed character representation.

- unsigned char
Type for unsigned character representation. Also used to inspect object representation (raw memory).

- char
Type for character representation which can be most efficiently processed on the target system (has the same representation and alignment as either signed char or unsigned char, but is always a distinct type). Multibyte characters strings use this type to represent code units. For every value of type unsigned char in range [0, 255], converting the value to char and then back to unsigned char produces the original value. (since C++11). The signedness of char depends on the compiler and the target platformL the dafaults for ARM and PowerPC are typically unsigned, the defaults fir x86 and x64 are typically signed.

- wchar_t
Type for wide character representation (see wide strings). Required to be large enough to represent any supported character code point (32 bits on systems that support Unicode. A notable exception is Windows, where wchar_t is 16 bits and holds UTF-16 code units) It has the same size, signedness, and alignment as one of the integer types, but is a distinct type.

- char16_t
- char32_t
- char8_t

### Floating Point Types
- float
- double
- long double

Keywords: void, bool, true, false, char, wchar_t, char8_t, char16_t, char32_t, int, short, long, signed, unsigned, float, double

## :books: Types in Windows
### Built-in Types (C++) | [MS Docs](https://docs.microsoft.com/en-us/cpp/cpp/fundamental-types-cpp?view=msvc-160)
- Void Type
- std::nullptr_t
- Boolean Type
- Character Types
- Floating-point Types
- Integer Types
  - Integer Type synonyms
- Sizes of Built-in Types

### Data Type Ranges | [MS Docs](https://docs.microsoft.com/en-us/cpp/cpp/data-type-ranges?view=msvc-160&viewFallbackFrom=vs-2019)
The Microsoft C++ 32-bit and 64-bit compilers recognize the types in the table later in this article.

- `int` (`unsigned int`)
- `__int8` (`unsigned __int8`)
- `__int16` (`unsigned __int16`)
- `__int32` (`unsigned __int32`)
- `__int64` (`unsigned __int64`)
- `short` (`unsigned short`)
- `long` (`unsigned long`)
- `long long` (`unsigned long long`)

If its name begins with two underscores (`__`), a data type is non-standard.

The ranges that are specified in the following table are inclusive-inclusive.
|Type Name|Bytes|Other Names|Range of Value|
|:-------:|:---:|:---------:|:------------:|
|int|4|signed|-2,147,483,648 to 2,147,483,647|
|unsigned int|4|unsigned|0 to 4,294,967,295|
|__int8|1|char|-128 to 127
|unsigned __int8|1|unsigned char|0 to 255|
|__int16|2|short, short int, signed short int|-32,768 to 32,767|
|unsigned __int16|2|unsigned short, unsigned short int|0 to 65,535|
|__int32|4|signed, signed int, int|-2,147,483,648 to 2,147,483,647|
|unsigned __int32|4|unsigned, unsigned int|0 to 4,294,967,295|
|__int64|8|long long, signed long long|-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807|
|unsigned __int64|8|unsigned long long|0 to 18,446,744,073,709,551,615|
|bool|1|none|false or true|
|char|1|none|-128 to 127 by default|
|signed char|1|none|-128 to 127|
|unsigned char|1|none|0 to 255|
|short|2|short int, signed short int|-32,768 to 32,767|
|unsigned short|2|unsigned short int|0 to 65,535|
|long|4|long int, signed long int|-2,147,483,648 to 2,147,483,647|
|unsigned long|4|unsigned long int|0 to 4,294,967,295|
|long long|8|none|-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807|
|unsigned long long|8|none|0 to 18,446,744,073,709,551,615|
|enum|varies|none|-|
|float|4|none|3.4E +/- 38 (7 digits)|
|double|8|none|1.7E +/- 308 (15 digits)|
|long double|same as double|none|same as double|
|wchar_t|2|__wchar_t|0 to 65,535|

### Windows Data Types | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/winprog/windows-data-types)
|Data Type|Description|
|:-------:|:---------:|
|-|-|

----------

## :books: String
### std::string | [cplusplus](https://www.cplusplus.com/reference/string/string/)
typedef basic_string<char> string;

String class

Strings are objects that represent sequences of characters.

The standard string class provides support for such objects with an interface similar to that of a standard container of bytes, but adding features specifically designed to operate with strings of single-byte characters.

The string class is an instantiation of the basic_string class template that uses char (i.e., bytes) as its character type, with its default char_traits and allocator types (see basic_string for more info on the template).

Note that this class handles bytes independently of the encoding used: If used to handle sequences of multi-byte or variable-length characters (such as UTF-8), all members of this class (such as length or size), as well as its iterators, will still operate in terms of bytes (not actual encoded characters).

### wcscmp() - Compare Wide Character Strings | [IMB i](https://www.ibm.com/docs/en//i/7.3?topic=functions-wcscmp-compare-wide-character-strings)
Format
```C++
#include <wchar.h>
int wcscmp(const whar_t *string1, const wchar_t *string2);
```
Language Level: ANSI. Threadsafe: Yes. The wcscmp() function compares two wide-character strings. The wcscmp() function operates on null-ended wchar_t strings; string arguments to this function should contain a wchar_t null character marking the end of the string. Boundary checking is not performed when a string is added to or copied.

## :books: Strings in Windows
### Working with Strings | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/learnwin32/working-with-strings)
Windows natively supports Unicode strings for UI elements, file names, and so forth. Unicode is the preferred character encoding, because it supports all character sets and languages. Windows represents Unicode characters using UTF-16 encoding, in which each character is encoded as a 16-bit value. UTF-16 characters are called wide characters, to distinguish them from 8-bit ANSI characters. The Visual C++ compiler supports the build-in data type wchar_t for wide characters. The header file WinNT.h also defines the following typedef.
```C++
typedef wchar_t WCHAR;
```
You wil see both versions in MSDN example code. To declare a wide-character literal or a wide-character string literal, put L before the literal.
```C++
wchar_t a = L'a';
wchar_t *str = L"hello";
```

### Windows Data Types for Strings | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/intl/windows-data-types-for-strings)
Most string operations can use the same logic for Unicode and for Windows code pages. The only difference is that the basic unit of operation is a 16-bit character (also known as a wide character) for Unicode and an 8-bit character for Windows code pages. The Windows header files provide several type definitions that make it easy to create sources that can be compiled for Unicode or for Windows code pages.

Windows supports three sets of character and string data types: a set of generic type definitions that can compile for either Unicode for Windows code pages, and two sets of specific type definitions. One set of specific type definitions is for use with Unicode, and the other is for use with Windows code pages.

An application using generic data types can be compiled for Unicode simply by defining "UNICODE" before the #include statements for the header files, or during compilation. New Windows applications should use Unicode to avoid the inconsistencies of varied code pages and to simplify localization. They should be written with generic data types, and should define "UNICODE" in order to compile these types into Unicode types. In the few places where an application must work with 8-bit character data, it can make explicit use of the types for Windows code pages.

The ability to compile the generic types into types for Windows code pages exists mainly to support legacy applications. To compile for Windows code pages, the application just omits the UNICODE definition.

The following example shows the method used in the Windows header files to define the three sets of data types. For the implementation, see the Winnt.h header file.

```C++
// Generic types
#ifdef UNICODE
    typedef wchar_t TCHAR;
#else
    typedef unsigned char TCHAR;
#endif
typedef TCHAR *LPTSTR, *LPTCH;
// 8-bit character specific
typedef unsigned char CHAR;
typedef CHAR *LPSTR, *LPCH;
// Unicode specific (wide characters)
typedef unsigned wchar_t WCHAR;
typedef WCHAR *LPWSTR, *LPWCH;
```

The letter "T" in a type definition, for example, TCHAR or LPTSTR, designates a generic type that can be compiled for either Windows code pages or Unicode. The letter "W" in a type definition, for example, WCHAR or LPWSTR, designates a Unicode type. Because Windows code pages are of the older form, they have simple type definitions, such as CHAR and LPSTR. For a complete description of data types in Windows, see Windows Data Types.

### Unicode in the Windows API | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/intl/unicode-in-the-windows-api)
Windows API functions that manipulate characters are generally implemented in one of three formats:
1. A generic version that can be compiled for either Windows code pages or Unicode.
2. A Windows code page verison with the letter "A" used to indicate "ANSI".
3. A Unicode version with the letter "W" used to indiate "wide".

### MultiByteToWideChar function (stringapiset.h) | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/api/stringapiset/nf-stringapiset-multibytetowidechar)

### WideCharToMultiByte function (stringapiset.h) | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/api/stringapiset/nf-stringapiset-widechartomultibyte)

----------

## :books: *Data Structure*

----------

### Standard Template Library(STL)
Library that provides data structure and algorithm as template

#### Algorithm
Is is a function template that provides a generalized way to solve sorts, deletes, searches, operations, etc.

#### Allocator
It is a class object that encapsulates a container's memory allocation policy. Every container has its own allocator.

#### Container
It also called an object or data structure that stores objects. It is implemented as a class template.

##### Associative Container
##### array
##### vector
##### list
##### deque
##### Sequence Container
##### set
##### multiset
##### map
##### multimap
##### Container Adaptor
It changes the component's interface to a component with a new interface.

##### stack
##### queue
##### Priority_queue
### *Function Object*
It is an object that behaves like a function, with the operator() operator overloaded. Client policy is reflected in containers and algorithms.

### *Iterator*
It is a function similar to a pointer that points to an element in a container, accesses the element it points to, and points to the next element.

### *untitled*

### *Operator*
### *Ternary Operator*
`Conditional statement ? return value 1 : return value 2`

If the conditional statment is true, return value 1 if it is false, return value 2.

## :books: Classes
### Constructors and member initializer lists | [cppreference](https://en.cppreference.com/w/cpp/language/constructor)
Constructor is a special non-static member function of a class that is used to initialize objects of its class type. In the definition of a constructor of a class, member initializer list specifies the initializers for direct and virtual bases and non-static data members. (Not to be confused with std::initializer_list.) A constructor must not be a coroutine. (since C++20)

#### Syntax
Constructors are declared using member function declarartors of the following form:
`class-name (parameter-list(optional)) except-spec(optional) attr(optional)`
Where class-name must name the current class (or current instantiaion of a class template), or, when declared at namespace scope or in a friend declaration, it must be a qualified class name.

## :books: Functions
### Coroutines (C++20) | [cppreference](https://en.cppreference.com/w/cpp/language/coroutines)
A coroutine is a function that can suspend execution to be resumed later. Coroutines are stackless: they suspend execution by returning to the caller and the data that is required to resume execution is stored separately from the stack. This allows for sequential code that executes asynchronously (e.g. to handle non-blocking I/O without explicit callbacks), and also supports algorithms on lazy-computed infinite sequences and other uses.

A function is a coroutine if its definition does any of the following:
- uses the co_await operator to suspend execution until resumed
```C++
task<> tcp_echo_server() {
    char data[1024];
    for (;;) {
        size_t n = co_await socket.async_read_some(buffer(data));
        co_await async_write(socket, buffer(data, n));
    }
}
```
- uses the keyword co_yield to suspend execution returning a value
```C++
generator<int> iota(int n=0) {
    while(ture)
        co_yield n++;
}
```
- uses the keyword to_return to complete execution returning a value
```C++
lazy<int> f() {
    co_return 7;
}
```
Every coroutine must have a return type that satifies a number of requirments.

#### `friend` Class
It can access to `private` and `protected member` to other `friend class`.

#### `friend` Function
Same as `friend class`, it gives other to access `private` and `protected member` with function unit not as class unit.

#### Static Variable (`static` as local variable)
It can use as global variable in corresponding source code, and keep after scope is ended, plus it only initialized for once and keeps until program end. It has same scope as local variable but alive until program end as global variable. 

### Template
It codes only `.h`s not `.cc`s.

#### Smart pointer
C++ provides smart pointer to guarantee program's secure with memory leak. It is class template works as pointer, it releases memory automatically when useless. There was `auto_ptr` before C++11, and after C++11, there are `unique_ptr`, `shared_ptr`, and `weak_ptr`.

#### boost::scoped_ptr
One of smart pointer, but restrained. It is same as `auto_ptr` without copying function.

### *typedef*
It can make nickname of type. For example, `typedef double d` means `d` is nickname of type `double`. It can't define new type.

### :books: sstream
### *istringstream*
It used to parse(input) string.

### ostringstream
It used to save(output) string.

### stringstream
It used to modifie data of string.

### :books: Call
### Call by Value
값에 의한 호출을 통해 메모리 공간에서는 함수를 위한 별도의 임시 공간 stack frame이 생성되고, 함수 호출 시 전달되는 변수의 값을 복사해서 함수의 인자로 전달한다. 복사된 인자는 함수 안에서 지역적으로 사용되는 local value의 특성을 가진다. 따라서 함수 안에서 인자의 값이 변경되어도, 외부의 변수 값은 변경되지 않는다.

큰 구조체 또는 클래스를 함수에 전달할 때 값으로 전달하면 인수의 복사본을 함수 매개 변수로 만든다. 이 경우 복사하는데 큰 비용이 들어 성능이 저하될 수 있다. 그리고 값으로 인수를 전달할 경우 함수에서 호출자에게 값을 반환하는 유일한 방법은 함수의 반환 값을 사용하는 것이다. 이 방법도 좋지만, 함수에서 인수를 수정하는 것이 더 명확하고 효율적일 수 있다.

### Call by Reference (Pass by Reference)
call by reference/pass by reference 참조로 전달하면 함수를 위한 별도의 임시 공간은 생성되지만, 함수 호출 시 인자로 전달되는 변수의 레퍼런스를 전달 받아 해당 변수를 가르키기 때문에 인자의 값이 변경되면 argument로 전달된 object의 값도 함께 변경된다.

### :books: Cast
### *C Style Cast* | [Explicit type conversion](https://en.cppreference.com/w/cpp/language/explicit_cast)
It can convert(cast) A type to B type, it can convert(cast) any type to any type.

- `(type-id)(e-pression)`
- `(new_type)expression`
- `new_type(expression)`
- `new_type(arg1, arg2, ...)`
- `new_type()`
- `new_type{arg1, arg2, ...(optional)}` since C++11
- `template-name(arg1, arg2, ...(optional))` since C++17
- `template-name{arg1, arg2, ...(optional)}` since C++17

### C++ Style Cast
It can convert(cast) A type to B type, it has to use right cast. `<type-id>(e-pression)`

### const_cast | [cppreference](https://en.cppreference.com/w/cpp/language/const_cast)
Converts between types with difference cv-qualificaion. It removes or grant constness to expression. It rarley used to grant constness to expression.

Syntax: `const_cast<new_type>(expression)`, returns a value of type new_type

#### dynamic_cast | [cppreference](https://en.cppreference.com/w/cpp/language/dynamic_cast)
Safely converts pointers and references to classes up, down, and sideways along the inheritance hierarchy. It is casting operator used to traverse inheritance hierarchy dynamically at run time or when downcasting. It casts pointer or reference's base class instance to derived class or sibling class type. It can't be casted between nonpolymorphic objects, and a compliation error occurs when attempting.

Syntax: `dynamic_cast<new_type>(expression)`, new_type: pointers to complete class type, reference to complete class type, or pointer to (optionally cv-qualified) void. expression: lvalue (until C++11) glvalue (since C++11) of a complete class type if new_type is a reference, prvalue of a pointer to complete class type if new_type is a pointer. If the cast is successful, dynamic_cast returns a value of type new_type. If the cast fails and new_type is a pointer type, it returns a null pointer of that type. If the cast fails and new_type is a reference type, it throws an exception that matches a handler of type std::bad_cast.

### reinterpret_cast | [cppreference](https://en.cppreference.com/w/cpp/language/reinterpret_cast)
Converts between types by reinterpreting the underlying bit pattern. It can convert/cast any type of pointer to any type of pointer, for example, pointer to integer or integer to pointer, everything is possible.

Syntax: `reinterpret_cast<new_type>(expression)`, returns a value of type new_type.

### *static_cast* | [cppreference](https://en.cppreference.com/w/cpp/language/static_cast)
Converts between types using a combination of implicit and user-defined conversions. It is basic cast as having same meaning and same ability to convert/cast as C style cast. It has limit as can't convert/cast struct type to int/double or float to pointer, and can't remove constness. It's name is because it checks its' type at moment of compile not at run-time.

Syntax: `static_cast<new_type>(expression)` returns a value of type new_type.

### *Constant Member Variable*
상수 멤버 변수란 한번 초기화하면, 그 값을 변경할 수 없는 멤버 변수이며 `const` 키워드를 사용한다. 문법으로는 `const type_name member_variable_name;`으로 쓴다.

### Constant Member Function
상수 멤버 함수란 호출한 객체의 데이터를 변경할 수 없는 멤버 함수이며 함수의 원형 마지막에 `const` 키워드를 사용하여 선언한다. 호출한 객체의 데이터를 단순히 읽기만 하는 멤버 함수는 상수 멤버 함수로 정의하는 것이 정보 보호 측면에서 좋다. `function_name const;`

### Function Name Mangling | [Blog (KR)](https://m.blog.naver.com/PostView.nhn?blogId=neokjc&logNo=60050291436&proxyReferer=https:%2F%2Fwww.google.com%2F)
C++에서는 함수 중복을 하기 때문에 함수 이름이 같더라도 구별되는 인자열에 따라 다른 이름을 만들어준다. 컴파일러가 어떤 일관된 규칙에 따라 함수를 부호화하는 것이다. 방법은 컴파일러마다 다르지만 The Annotated C++ Reference Manual에 name encoding이라는 내용이다.

### :books: Function Keyword

### virtual
It used to declare function virtually in parent class, and it make child class declare in real. It used to manage modules as component, as modules have one same parent and make class as themselves with specify along their property.

### override
This keyword used at child class's virtual function, as `virtual` keyword is used front of function and at parent class, but `override` keyword is used end of function and at child class. Plus, `final` keyword is used at the last child class, and it means there will be no more virtual function over riding.

### overloading

### Initialize Function Argument
- foo.h
```C++
void foo(int bar = 0);
```

### :books: Keyword
### ->
포인터 변수의 값을 참조하기 위한 연산자이다.

```C++
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

### #if #elif #else #endif
```C++
#if condition1
function1();

#elif condition2
function2();

#else
function3();

#endif
```

### :books: Namespaces | [MS Docs](https://docs.microsoft.com/en-us/cpp/cpp/namespaces-cpp?view=msvc-160)
A namespace is a declarative region that provides a scope to the identifiers (the names of types, functions, variables, etc) inside it. Namespaces are used to organize code into logical groups and to prevent name collisions that can occur expecially when your code base includes multiple libraries. All identifiers at namespace scope can access the members by using the fully qualified name for each identifier, for example `std::vector<std::string> vec;` or else by a using Declaration for a single identifier (`using std::string`), or a using Directive for all the identifiers in the namespace (`using namespace std;`). Code in header files should always use the fully qualified namespace name.

### Using Directives

### Declaring Namespaces and Namespace Members

### The Global Namespace
If an identifier is not declared in an explicit namespace, it is part of the implicit global namespace. In general, try to avoid making declarations at global scope when possible, except for the entry point main Function, which is required to be in the global namespace. To explicitly qualify a global identifier, use the scope resolution operator with no name, as in `::SomeFunction(x);`. This will differentiate the identifier from anything with the same name in any other namespace, and it will also help to make you code easier for others to understand.

### The std Namespace

### Nested Namespaces
Namespaces may be nested. An ordinary nested namespace has unqualified access to its parent's members, but the parent members do not have unqualified access to the nested namespace (unless it is declared as inline), as shown in the following example:
```C++
namespace ContosoDataServer
{
    void Foo();
    namespace Details
    {
        int CountImpl;
        void Ban() {return Foo();}
    }
    
    int Bar(){..};
    int Baz(int i) {return Details::CountImpl;}
}
```
Ordinary nested namespaces can be used to encapsulate internal implementation details that are not part of the public interface of the parent namespace.

### Namespace Aliases
Namespace names need to be unique, which means that often they should not be too short. If the length of a name makes code difficult to read, or is tedious to type in a header file where using directives can't be used, then you can make a namespace alias which serves as an abbreviation for the actual name. For example:
```C++
namespace a_very_long_namespace_name {class Foo {};}
namespace AVLNN == a_very_long_namespace_name;
void Bar(AVLNN::FOO foo){ }
```
### Inline namespaces (C++ 11)

### Anonymous or Unnamed Namespaces
You can create an explicit namespace but not give it a name:
```C++
namespace
{
    int MyFunc() {}
}
```
This is called an unnamed or anonymous namespace and it is useful when you want to make variable declarations invisible to code in other files (i.e. give them internal linkage) without having to create a named namespace. All code in the same file can see the identifiers in an unnamed namespace but the identifiers, along with the namespace itself, are not visible outside that file-or more precisely outside the translation unit.

### *Static Member Variable*
정적 멤버 변수는 클래스에는 속하지만 객체 별로 할당되지 않고 클래스의 모든 객체가 공유한다. 해당 클래스의 모든 객체에 대해 하나의 데이터만이 유지 관리된다. 선언은 클래스 영역에서 되지만, 정의는 파일 영역에서 수행된다. 이러한 정적 멤버 변수는 외부 연결을 가지므로, 여러 파일에서 접근할 수 있다.

정적 멤버 변수에도 클래스 멤버의 접근 제한 규칙이 적용되므로, 클래스의 멤버 함수나 프렌드만이 접근할 수 있다. 하지만 외부에서도 접근할 수 있게 하고 싶으면, public 영역에 선언하면 된다.

### Static Member Function
정적 멤버 함수는 해당 클래스의 객체를 생성하지 않고도, 클래스 이름만으로 호출할 수 있다. 문법으로는 `object_name.member_function_name();`는 일반 멤버 함수의 호출이고, `class_name.member_function_name();`으로도 호출 가능하다. 정적 멤버 함수는 정적 멤버 변수를 선언하는 방법과 같이 static 키워드를 사용해서 선언한다. 특징으로는 객체를 생성하지 않고 클래스 이름만으로 호출 가능하며, 객체를 생성하지 않으므로 this 포인터를 가지지 않고, 특정 객체와 결합하지 않으므로 정적 멤버 변수만 사용 가능하다.

### struct (C++) | [MS Docs](https://docs.microsoft.com/en-us/cpp/cpp/struct-cpp?view=msvc-160)
The struct keyword defines a structure type and/or a variable of a structure type.
```C++
[template-spec] struct [ms-decl-spec] [tag [: base-list ]]
{
    member-list
} [declarators];
[struct] tag decalarators;
```

##### Static Versus Dynamic Binding

##### Forward Declarartions and Definitions

##### Extern Versus Static Versus Class Static

##### Singleton

##### GetDriveType()

##### std::vector<type>
    
##### std::map<type, type>

## :books: C++ Language Reference | [MS Docs](https://docs.microsoft.com/en-us/cpp/cpp/cpp-language-reference?view=msvc-160)

### Keywords | [MS Docs](https://docs.microsoft.com/en-us/cpp/cpp/keywords-cpp?view=msvc-160)
Keywords are predefined reserved identifiers that have special meanings. They can't be used as identifiers in your program. The following keywords are reserved for Microsoft C++. Names with leading underscores and names specified for C++/CX and C++/CLI are Microsoft extensions.

### Operators | [MS Docs](https://docs.microsoft.com/en-us/cpp/cpp/cpp-built-in-operators-precedence-and-associativity?view=msvc-160)
The C++ language includes all C operators and adds several new operators. Operators specify an evaluation to be performed on one or more operands.

## :books: C/C++ Preprocessor Reference | [MS Docs](https://docs.microsoft.com/en-us/cpp/preprocessor/c-cpp-preprocessor-reference?view=msvc-160)
The C/C++ preprocessor reference explains the preprocessor as it is implemented in Microsoft C/C++. The preprocessor performs preliminary operations on C and C++ files before they are passed to the compiler. You can use the preprocessor to conditionally compile code, insert files, specify compile-time error messages, and apply machine-specific rules to sections of code.

In Visual Studio 2019 the /Zc:preprocessor compiler options provides a fully conformant C11 and C17 preprocessor. This is the default when you use the compiler flag `/std:c11` or `/std:c17`.

### Preprocessor | [MS Docs](https://docs.microsoft.com/en-us/cpp/preprocessor/preprocessor?view=msvc-160)
The preprocessor is a text processor that manipulates the text of a source file as part of the first phase of translation. The preprocessor doesn't parse the source text, but it does break it up into tokens to locate macro calls. Although the compiler ordinarily invokes the preprocessor in its first pass, the preprocessor can also be invoked separately to process text without compiling.

### Preprocessor Directives | [MS Docs](https://docs.microsoft.com/en-us/cpp/preprocessor/preprocessor-directives?view=msvc-160)
Preprocessor directives, such as `#define` and `#ifdef`, are typically used to make source programs easy to change and easy to compile in different execution environments. Directives in the source file tell the preprocessor to take specific actions. For example, the preprocessor can replace tokens in the text, insert the contents of other files into the source file, or suppress compilation of part of the file by removing sections of text. Preprocessor lines are recognized and carried out before macro expansion. Therefore, if a macro expands into something that looks like a preprocessor command, it isn't recognized by the preprocessor.

Preprocessor statements use the same character set as source file statements, with the exception that escape sequences aren't supported. The character set used in preprocessor statements is the same sa the execution character set. The preprocessor also recognizes negative character values.

The preprocessor recognizes the following directives: `#define`, `#elif`, `#else`, `#endif`, `#error`, `#if`, `#ifdef`, `#ifndef`, `#import`, `#include`, `#line`, `#pragma`, `#undef`, `#using`

The number sign (`#`) mush be the first nonwhite-space character on the line containing the directive. White-space characters can appear between the number sign and the first letter of the directive. Some directives include arguments or values. Any text that follows a directive (except an argument or value that is part of the directive) must be preceded by the single-line commet delimiter (`//`) or enclosed in comment delimiters (`/* */`). Lines containing preprocessor directives can be continued by immediately preceding the end-of-line market with a backslash (`\`).

Preprocessor directives can appear anywhere in a source file, but they apply only to the rest of the source file, after they apper.

### #if, #elif, #else, and #endif directives (C/C++) | [MS Docs](https://docs.microsoft.com/en-us/cpp/preprocessor/hash-if-hash-elif-hash-else-and-hash-endif-directives-c-cpp?view=msvc-160)
The `#if` directive, with the `#elif`, `#else`, and `#endif` directives, controls compilation of portions of a source file. If the expression you write (after the `#if`) has a nonzero value, the line group immediately following the `#if` directives is kept in the translation unit.

### Preprocessor Operator defined

### Preprocessor Operator __has_include

### #ifdef and #ifndef directives (C/C++) | [MS Docs](https://docs.microsoft.com/en-us/cpp/preprocessor/hash-ifdef-and-hash-ifndef-directives-c-cpp?view=msvc-160)
The `#ifdef` and `#ifndef` preprocessor directives have the same effect as the `#if` directive when it's used with the `defined` operator.

Syntax: 
```C++
#ifdef identifier
#ifndef identifier
```
These directives are quivalent to:
```C++
#if defined identifier
#if !defined identifier
```
The `#ifdef` directive is useful for checking whether a definition exists, because a definition can be passed from the command line. For example:
```C++
// ifdef_ifndef.CPP
// compile with: /Dtest /c
#ifndef test
#define final
#endif
```

### Macros (C/C++) | [MS Docs](https://docs.microsoft.com/en-us/cpp/preprocessor/macros-c-cpp?view=msvc-160)
The preprocessor expands macros in all lines except preprocessor directives, lines that have a # as the first non-white-space character. It expands macros in parts of some directives that aren't skipped as part of a conditional compilation. Conditional compilation directives allow you to suppress compilation of parts of a source file. They test a constant expression or identifier to determine which text blocks to pass on the the compiler, and which ones to remove from the source file during preprocessing.

The #define directive is typically used to associate meaningful identifiers with constant, keywords, and commonly used statements or expressions. Identifiers that represent constants are sometimes called symbolic constants or manifest constants. Identifiers that represent statements or expressions are called macros. In this preprocessor documentation, only the term "macro" is used.

### once pragma | [MS Docs](https://docs.microsoft.com/en-us/cpp/preprocessor/once?view=msvc-160)
Specifices that the compiler includes the header file only once, when compiling a source code file.

Syntax: `#pragma once`

### TEXT macro (winnt.h) | [MS Docs](https://docs.microsoft.com/en-us/windows/win32/api/winnt/nf-winnt-text)
Identifies a string as Unicode when UNICODE is defined by a preprocessor directive during compilation. Otherwise, the macro identifies a string as an ANSI string.

Syntax: `void TEXT(quote);`. `quote`: Pointer to the string to interpret as UTF-16 or ANSI. Return value: None.

----------
  
## :books: Pattern

### Resource Acquisition Is Initialization (RAII)

----------

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
- GetDriveType(), https://docs.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-getdrivetypea, 2021-01-06-Wed.
- Exception Handling Blog KR, https://blog.hexabrain.net/179, 2021-04-12-Mon.
- Function name mangling Blog KR, https://m.blog.naver.com/PostView.nhn?blogId=neokjc&logNo=60050291436&proxyReferer=https:%2F%2Fwww.google.com%2F, 2021-04-14-Wed.
- struct, http://www.tcpschool.com/cpp/cpp_struct_intro, 2021-04-16-Fri.
- struct Blog KR, https://boycoding.tistory.com/183, 2021-04-16-Fri.
- struct, https://docs.microsoft.com/en-us/cpp/cpp/struct-cpp?view=msvc-160, 2021-04-16-Fri.
- string append Blog, https://modoocode.com/307, 2021-04-20-Tue.
- C++ explicit_cast, https://en.cppreference.com/w/cpp/language/explicit_cast, 2021-04-26-Mon.
- C++ static_cast, https://en.cppreference.com/w/cpp/language/static_cast, 2021-04-26-Mon.
- C++ dynamic_cast, https://en.cppreference.com/w/cpp/language/dynamic_cast, 2021-04-26-Mon.
- C++ const_cast, https://en.cppreference.com/w/cpp/language/const_cast, 2021-04-27-Tue.
- C++ reinterpret_cast, https://en.cppreference.com/w/cpp/language/reinterpret_cast, 2021-04-27-Tue.
- Namespaces MS Docs, https://docs.microsoft.com/en-us/cpp/cpp/namespaces-cpp?view=msvc-160, 2021-04-27-Tue.
- C/C++ #ifdef and #ifndef directives, https://docs.microsoft.com/en-us/cpp/preprocessor/hash-ifdef-and-hash-ifndef-directives-c-cpp?view=msvc-160, 2021-04-28-Wed.
- C/C++ Macros, https://docs.microsoft.com/en-us/cpp/preprocessor/macros-c-cpp?view=msvc-160, 2021-04-28-Wed.
- Preprocessor Directives, https://docs.microsoft.com/en-us/cpp/preprocessor/preprocessor-directives?view=msvc-160, 2021-04-28-Wed.
- C/C++ #if, #elif, #else, and #endif directives, https://docs.microsoft.com/en-us/cpp/preprocessor/hash-if-hash-elif-hash-else-and-hash-endif-directives-c-cpp?view=msvc-160, 2021-04-28-Wed.
- once pragma, https://docs.microsoft.com/en-us/cpp/preprocessor/once?view=msvc-160, 2021-04-28-Wed.
- C/C++ Preprocessor Reference, https://docs.microsoft.com/en-us/cpp/preprocessor/c-cpp-preprocessor-reference?view=msvc-160, 2021-04-28-Wed.
- C++ Language Reference, https://docs.microsoft.com/en-us/cpp/cpp/cpp-language-reference?view=msvc-160, 2021-04-28-Wed.
- C++ Keywords, https://docs.microsoft.com/en-us/cpp/cpp/keywords-cpp?view=msvc-160, 2021-04-28-Wed.
- C++ Operators, https://docs.microsoft.com/en-us/cpp/cpp/cpp-built-in-operators-precedence-and-associativity?view=msvc-160, 2021-04-28-Wed.
- Preprocessor, https://docs.microsoft.com/en-us/cpp/preprocessor/preprocessor?view=msvc-160, 2021-04-28-Wed.
- Data Type Ranges, https://docs.microsoft.com/en-us/cpp/cpp/data-type-ranges?view=msvc-160&viewFallbackFrom=vs-2019 2021-05-04-Tue.
- Windows Data Types, https://docs.microsoft.com/en-us/windows/win32/winprog/windows-data-types, 2021-05-04-Tue.
- Built-in Types, https://docs.microsoft.com/en-us/cpp/cpp/fundamental-types-cpp?view=msvc-160, 2021-05-04-Tue.
- TEXT macro (winnt.h), https://docs.microsoft.com/en-us/windows/win32/api/winnt/nf-winnt-text, 2021-05-12-Wed.
- Working with Strings, https://docs.microsoft.com/en-us/windows/win32/learnwin32/working-with-strings, 2021-05-12-Wed.
- Constructors and member initializer lists, https://en.cppreference.com/w/cpp/language/constructor, 2021-05-14-Fri.
- Coroutines (C++20), https://en.cppreference.com/w/cpp/language/coroutines, 2021-05-14-Fri.
- Windows Data Types for Strings, https://docs.microsoft.com/en-us/windows/win32/intl/windows-data-types-for-strings, 2021-05-21-Fri.
- Unicode in the Windows API, https://docs.microsoft.com/en-us/windows/win32/intl/unicode-in-the-windows-api 2021-05-21-Fri.
- Encoding Blog KR, https://onlywis.tistory.com/2 2021-05-21-Fri.
- std::string, https://www.cplusplus.com/reference/string/string/, 2021-05-21-Fri.
- Fundamental Types, https://en.cppreference.com/w/cpp/language/types, 2021-05-21-Fri.
- MultiByteToWideChar function (stringapiset.h), https://docs.microsoft.com/en-us/windows/win32/api/stringapiset/nf-stringapiset-multibytetowidechar, 2021-05-24-Mon.
- WideCharToMultiByte function (stringapiset.h), https://docs.microsoft.com/en-us/windows/win32/api/stringapiset/nf-stringapiset-widechartomultibyte, 2021-05-24-Mon.
- wcscmp(), https://www.ibm.com/docs/en//i/7.3?topic=functions-wcscmp-compare-wide-character-strings, 2021-05-25-Tue.
- RAII Pattern Blog KR, https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kmc7468&logNo=220989121076, 2021-06-15-Tue.

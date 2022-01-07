# JavaScript | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)
JavaScript (or "JS") is a programming language used most often for dynamic client-side scripts on webpages, but it is also often used on the server-side, using a runtime such as Node.js.

JavaScript should not be confused with the Java programming language. Althought "Java" and "JavaScript" are trademarks (or registered trademarks) of Oracle in the U.S. and other countires, the two programming languages are significantly different in their syntax, semantics, and use cases.

JavaScript is primarily used in the browser, enabling developers to manipulate webpage content through the DOM, manipulate data with AJAX and IndexedDB, draw graphics with canvas, interact with the device running the browser through various APIs, and more. JavaScript is one of the world's most commonly-used languages, owing to the recent growth and performance improvement of APIs available in browsers.

----------

# JavaScript basics | [MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
JavaScript is a programming language that adds interactivity to your website. This happens in games, in the behavior of responses when buttons are pressed or with data entry on forms; with dynamic styling; with animation, etc. This article helps you get started with JavaScript and futhers your understanding of what is possible.

## What is JavaScript?
JavaScript("JS" for short) is a full

## A Hello world! example

### What happened?

## Language basics crash course

### Variables
Variables are containers that store values. You start by declaring a variable with the `var` (less recommended, dive deeper for the explanation) or the `let` keyword, followed by the name you give to the variable:
```JavaScript
let myVariable;
```
Note: A semicolon at the end of a line indicates where a statement ends. It is only required when you need to separate statements on a single line. However, some people believe it's good practice to have semicolons at the end of each statement. There are other rules for when you should and shouldn't use semicolons. [Your Guide to Semicolons in JavaScript](https://news.codecademy.com/your-guide-to-semicolons-in-javascript/)

Note: you can name a variable nearly anything, but there are some restirctions. [naming rules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables), or [check your variable name](https://mothereff.in/js-variables) to see if it's valid.

Note: JavaScript is case sensitive. This means `myVariable` is not the same as `myvariable`.

Note: For more details about the difference between `var` and `let`, see [The difference between var and let](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables#the_difference_between_var_and_let).

After declaring a variable, you can give it a value. Also you can do both these operations on the same line. You retrieve the value by calling the variable name. After assigning a value to a variable, you can change it later in the code. Note that variables may hold values that have different data types.

### Comments
Comments are snippets of text that can be added along with code. The browser ignores text marked as comments. You can write comments in JavaScript just as you can in CSS. `/* */`. If your commment contains no line breaks, it's an option to put it behind two slashs like `//`.

### Operators

### Conditionals

### Functions

### Events
Real interactivity on a website requires event handlers. These are code structures that listen for activity in the browser, and run code in response. The most obvious example is handling the click event, which is fired by the browser when you click on something with your mouse. To demonstrate this, entire the following into your console, then click on the current webpage:
```JavaScript
document.querySelector('html').onclick = function() {
  alert('Ouch! Stop poking me!');
}
```
There are many ways to attach an event handler to an element. Here we select the `<html>` element, setting its `onclick` handler property equal to an anonymous (i.e., nameless) function, which contains the code we want the click event to run.

Note that
```JavaScript
document.querySelector('html').onclick = function() {};
```
is equivalent to
```JavaScript
let myHTML = document.querySelector('html');
myHTML.onclick = function() {};
```
It's just shorter.

## Supercharging our example website

### Adding an image changer

### Adding a personalized welcome message

### A user name of null?

----------

## Data Type | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
The set if types in the JavaScript language consists of primitive values and objects. ECMAScript has two built-in numeric types: Number and BigInt.

### Dynamic typing
JavaScript is a loosely types and dynamic language. Variables in JavaScript are not directly associated with any particular value type, and any variable can be assigned (and re-assigned) values of all types.

```JavaScript
let foo = 42; // foo is now a number.
foo = 'bar';  // foo is now a string.
foo = true;   // foo is now a boolean. 
```

### Primitive Value
Immutable datum represented directly at the lowest level of the language. All types except objects define immutable values (that is, values which can't be changed). For example (and unlike in C), Strings are ummutable. We refer to values of these types as "primitive values".

### Boolean | [Glossary](https://developer.mozilla.org/en-US/docs/Glossary/Boolean) | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean)
Boolean represents a logical entity and can have two values: true and false.

### Null | [Glossary](https://developer.mozilla.org/en-US/docs/Glossary/Null) | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null)
The Null type has exactly one value: null.

### Undefined | [Glossary](https://developer.mozilla.org/en-US/docs/Glossary/undefined) | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
A variable that has not been assigned a value has the value undefined.

### Number
The Number type is a double-precision 64-bit binary format IEEE 754 value ( -(2^53)-1 ~ (2^53)-1). In addition to representing floating-point numbers, the number type has three symbolic values: +Infinity, -Infinity, and NaN (Not a Number)

### BigInt
The BigInt type is a numeric primitive in JavaScript that can represent integers with arbitrary percision. With BigInts, you can safely store and operate on large integers even beyond the safe integer limit for Numbers. A BigInt is created by appending n to the end of an integer or by calling the constructor.

```JavaScript
const x = 2n ** 53n; // 9007199254740992n
const y = x + 1n; // 9007199254740993n
```

You can use the operators +, -, *, **, and % with BinInts - just like with Numbers. A BigInt is not strictly equal to a Number, but it is lossely so. A BigInt behaves like a Number in cases where it is converted to boolean: if, ||, &&, Boolean, !. BigInts cannot be operated on interchangeably with Numbers. Instead a TypeError will be thrown.

### String
JavaScript's String type is used to represent textual data. It is a set of "elements" of 16-bit unsigned integer values. Each element in the String occupies a position in the String. The first element is at index 0, the next at index 1, and so on. The length of a String is the number of elements in it. Unlike some programming languages (such as C), JavaScript strings are immutable. This means that once a string is created, it is not possible to modify it. However, it is still possible to create another string based on operation on the original string. For example: a substring of the original by picking individual letters or using `String.substr()`. A concatenation of two strings using the concatenation operator (`+`) or `String.concat()`

### Symbol | [Glossary](https://developer.mozilla.org/en-US/docs/Glossary/Symbol) | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol) | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Symbol)
A symbol is a unique and immutable primitive value and may be used as the key of an Object property. In some programming languages, Symbols are called "atoms".

A value having the data type Symbol can be referred to as a "Symbol value". In a JavaScript runtime environment, a symbol value is created by invoking the function Symbol, which dynamically produces an anonymous, unique value. A symbol may be used as an object property. Symbol can have an optional description, but for debugging purposes only. A Symbol value represents a unique identifier.

```JavaScript
// Here are two symbols with the same description:
let Sym1 = Symbol("Sym")
let Sym2 = Symbol("Sym")

console.log(Sym1 === Sym2) // returns "false"
// Symbols are guaranteed to be unique. Even if we create many symbols with same description, they are different values.
```

If you are familiar with Ruby (or another language) that also has a feature called "symbols", please don't be missed. JavaScript symbols are different. Symbol type is a new feature in ECMAScript 2015. There is no ECMAScript 5 equivalent for Symbol. 

### Objects
Collections of properties. In computer science, an object is a value in memory which is possibly referenced by an identifier.

### Properties
In JavaScript, objects can be seen as a colleciton of properties. With the object literal syntax, a limited set of properties are initialized; then properties can be added and removed. Property values can be values of any type, including other objects, which enables building complex data structures. Properties are identified using key vales. A key value is either a String value or Symbol value.

Each property has corresponding attributes. Attributes are used internally by the JavaScript engine, so you cannot directly access them. That's why attributes are listed in double square brackets(`[[]]`), rather than single(`[]`). 

### Object.entires() | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries)
The Object.entries() method returns an array of a given object's own enumerable string-keyed property [key, value] pairs. This is the same as iterating with a for..in loop, except that a for...in loop enumerates properties in the prototype chain as well. 

```JavaScript
Object.entries(obj)
```

- Parameters
  - obj: The object whose own enumerable string-keyed property [key, value] pairs are to be returned.
- Return value
  - An array of the given object's own enumerable string-keyed property [key, value] pairs.

### Map | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
The Map object holds key-value pairs and remembers the original insertion order of the keys. Any value (both objects and primitive values) may be used as either a key or a value.

A Map object iterates its elements in insertion order - a `for...of` loop returns an array of `[key, value]` for each iteration.

### Objects vs. Maps
Object is similar to Map - both let you set keys to values, retrieve those values, delete keys, and detect whether something is stored at a key. For this reason (and because there were no built-in alternatives), Object has been used as Map historically. However, there are important differences that make Map preferable in some cases: Accidental Keys, Key Types, Key Order, Size, Iteration, Performance, Serialization and parsing.

----------

## [A re-introduction to JavaScript (JS tutorial)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)
JavaScript was created in 1995 by Brendan Eich while he was an engineer at Netscape. JavaScript was first released with Netscape 2 early in 1996. It was originally going to be called LiveScript, but it was renamed in an ill-fated marketing decision that attempted to capitalize on the popularity of Sun Microsystem's Java language - despite the tow having very little in common. This has been a source of confusion ever since.

Several months later, Microsoft released JScript with Internet Explorer 3. It was a mostly-compatible JavaScript work-alike. Several months after that, Netscape submitted JavaScript to Ecma International, a European standards organization, which resulted in the first edition of the ECMAScript standard that year. The standard received a significant update as ECMAScript edition 3 in 1999, and it has stayed pretty much stable ever since. The fourth edition was abandoned, due to political differences concerning language complexity. Many parts of the fourth edition formed the basis for ECMAScript edition 5, published in December of 2009, and for the 6th major edition of the standard, published in June of 2015.

Note: Because it is more familiar, it will refer to ECMAScripts as "JavaScript".

Unlike most programming languages, the JavaScript language has no concept of input or output. It is designed to run as a scripting language in a host environment, and it is up to the host environment to provide mechanisms for communicating with the outside world. THe most common host environment is the browser, but JavaScript interpreters can also be found in a huge list of other places, including Adobe Acrobat, Adobe Photoshop, SVG images, Yahoo's Widget engine, server-side environments such as Node.js, NoSQA databases like the open source Apache CouchDB, embedded computers, complete desktop environments like GNOME (one of the most popular GUIs for GNU/Linux operating systems), and others.

### Overview
JavaScript is a multi-paradigm, dynamic language with types and operators, standard built-in objects, and methods. Its syntax is based on the Java and C languages - many structures from those languages apply to JavaScript as well. JavaScript supports object-oriented programming with object prototypes, instead of classes (see more about prototypical inheritance and ES2015 classes). JavaScript also supports functional programming - because they are objects, functions may be stored in variables and passed around like any other object.

Let's start off by looking at the building blocks of any language: the types. JavaScript programs manipulate values, and those values all belong to a type. JavaScript's types are:

- Number
- BigInt
- String
- Boolean
- `Function`
- Object
- Symbol (new in ES2015)

... oh, and undefined and null, which are .. slightly odd. And `Array`, which is a special kind of object. And `Date` and `RegExp`, which are objects that you get for free. And to be technically accurate, functions are just a special type of object. So the type diagram looks more like this:

- Number
- BigInt
- String
- Boolean
- Symbol (new in ES2015)
- Object
  - `Function`
  - `Array`
  - `Date`
  - `RegExp`
- null
- undefined

And there are some built-in `Error` types as well. Things are a lot easier if we stick with the first diagram, however, so we'll discuss the types listed there for now. 

### Numbers

### Strings

### Other types

### Variables

### Operators

### Control structures

### Objects
JavaScript objects can be thought of as simple collections of name-value pairs. As such, they are similar to:
- Dictionaries in Python.
- Hashes in Perl and Ruby.
- Hash tables in C and C++.
- HashMaps in Java.
- Associative arrays in PHP.

The fact that this data structure is so widely used is a testament to its versatility. Since everything (bar core types) in JavaScript is an object, any JavaScript program naturally involves a great deal of hash table lookups. It's a good thing they're so fast.

The "name" part is a JavaScript string, while the value can be any JavaScript value - including more objects. This allows you to build data structures of arbitrary complexity.

There are tow basic ways to create an empty object:
```JavaScript
var obj = new Object();
```
And:
```JavaScript
var obj = {};
```
These are semantically equivalent; the second is called object literal syntax and is more convenient. This syntax is also the core of JSON format and should be preferred at all times.

Object literal syntax can be used to initialize an object in its entirety:
```JavaScript
var obj = {
    name: 'Carrot',
    _for: 'Max', // 'for' is a reserved word, use '_for' instead.
    details: {
        color: 'orange',
        size: 12
    }
};
```
Attribute access can be chained together:
```JavaScript
obj.details.color; // orange
obj['details']['size']; // 12
```
The following example creates an object prototype(`Person`) and an instance of that prototype(`you`).
```JavaScript
function Person(name, age) {
    this.name = name;
    this.age = age;
}

// Define an object
var you = new Person('You', 24);
// We are creating a new person named "You" aged 24.
```
Once created, an object's properties can again be accessed in one of two ways:
```JavaScript
// dot notation
obj.name = 'Simon';
var name = obj.name;
```
And...
```JavaScript
// bracket notation
obj['name'] = 'Simon';
var name = obj['name'];
// can use a variable to define a key
var user = prompt('what is your key?')
obj[user] = prompt('what is its value?')
```
These are also semantically equivalent. The second method has the advantage that the name of the property is provided as a string, which means it can be calculated at run-time. However, using this method prevents some JavaScript engine and minifier optimizations being applied. It can also be used to set and get properties with names that are reserved words:
```JavaScript
obj.for = 'Simon'; // Syntax error, because 'for' is a reserved word
obj['for'] = 'Simon'; // works fine
```
Note: Starting in ECMAScript 5, reserved words may be used as object property names "in the buff". This means that they don't need to be "clothed " in quotes when defining object literals. See the ES5 Spec.

For more on objects and prototypes see Object.prototype. For an explanation of object prototypes and the object prototype chains see Inheritance and the prototype chain.

Note: Starting in ECMAScript 2015, object keys can be defined by the variable using bracket notation upon being created. `{[phoneType]: 12345}` is possible instead of just `var userPhone = {};` `userPhone[phoneType] = 12345`.

### Arrays

### Functions
Along with objects, functions are the core component in understanding JavaScript. The most basic function couldn't be much simpler.
```JavaScript
function add(x, y) {
    var total = x + y;
    return total;
}
```
This demonstrates a basic function. A JavaScript function can take 0 or more named parameters. The function body can contain as many statements as you like an can declare its own variables which are local to that function. The `return` statement can be used to return a value at any time, terminating the function. If no return statement is used (or an empty return with no value), JavaScript returns `undefined`.

The named parameters turn out to be more like guidelines than anything else. You can call a function without passing the parameters it expects, in which case they will be set to `undefined`.
```JavaScript
add(); // NaN
// You can't perform addition on undefined
```
You can also pass in more arguments that the function is expecting:
```JavaScript
add(2, 3, 4); // 5
// added the first two; 4 was ignored
```
That may seem a little silly, but functions have access to an additional variable inside their body called `arguments`, which is an array-like object holding all of the values passed to the function. Let's re-write the add function to take as many values as we want:
```JavaScript
function add() {
    var sum = 0;
    for (var i = 0, j = arguments.length; i < j; i++) {
        sum += arguments[i];
    }
    return sum;
}

add(2, 3, 4, 5); // 14
```
That's really not any more useful than writing `2 + 3 + 4 + 5` though. Let's create an averaging function:
```JavaScript
function avg() {
    var sum = 0;
    for (var i = 0, j = arguments.length; i < j; i++) {
        sum += arguments[i];
    }
    return sum / arguments.length;
}

avg(2, 3, 4, 5); // 3.5
```
This is pretty useful, but it does seem a little verbose. To reduce this code a bit more we can look at substituting the use of the arguments array through Rest parameter syntax. In this way, we can pass in any number of arguments into the function while keeping our code minimal. The rest parameter operator is used in function parameter lists with the format: ...variable and it will include within that variable the entire list of uncaptured arguments that the function was called with. We will also repace the for loop with a for...of loop to return the values within our variable.
```JavaScript
function avg(...args) {
    var sum = 0;
    for (let value of args) {
        sun += value;
    }
    return sum / args.length;
}

avg(2, 3, 4, 5) // 3.5
```
In the above code, the variable args holds all the values that were passed into the function.

It is important to note that wherever the rest parameter operator is placed in a function declaration it will store all arguments after its declaration, but not before. i.e. function avg(firstValue, ...args) will store the first value passed into the function in the firstValue variable and the remaining arguments in args. That's another useful language feature but it does lead us to a new problem. The `avg()` function takes a common-separated list of arguments - but what if you want to find the average of an array? You could just rewrite the function as follows:
```JavaScript
function avgArray(arr) {
    var sum = 0;
    for (var i = 0 , j = arr.length; i < j; i++) {
        sum += arr[i];
    }
    return sum / arr.length;
}

avgArray([2, 3, 4, 5]); // 3.5
```
But it would be nice to be able to reuse the function that we've already created. Luckily, JavaScript lets you call a function with an arbitrary array of arguments, using the `apply()` method of any function object.
```JavaScript
avg.apply(null, [2, 3, 4, 5]); // 3.5
```
The second argument to `apply()` is the array to use as arguments; the first will be discussed later on. This emphasizes the fact that functions are objects too.

You can achieve the same result using the spread operator in the function call.

For instance: `avg(...numbers)`

#### Anonymous functions
JavaScript lets you create anonymous functions - that is, functions without names:
```JavaScript
function() {
    var sum = 0;
    for (var i = 0, j = arguments.length; i < j; i++) {
        sum += arguments[i];
    }
    return sum / arguments.length;
};
```
But such an anonymous function isn't useful in isolation - because without a name, there's no way to call the function. So in practice, anonymous functions are typically used as arguments to other functions or are made callable by immediately assigning them to a variable that can be used in invoke the function:
```JavaScript
var avg = function() {
    var sum = 0;
    for (var i = 0, j = arguments.length; i < j; i++) {
        sum += arguments[i];
    }
    return sum, / arguments.length;
};
```
That makes the anonymous function invocable by calling `avg()` with some arguments - that is, it's semantically equivalent to declaring the function using the `function avg()` named-function form.

But there's a way that anonymous functions can be useful even without ever being assigned to variables or passed as arguments ot other functions: JavaScript provides a mechanism for simultaneously declaring and invoking a function using a single expression. It's called an Immediatedly invoked function expression (IIFE), and the syntax for using it with an anonymous function looks like this:
```JavaScript
(function() {
    // ...
}) ();
```
Further details on IIFEs are out of scope for this introductory article - but a good example of what they're particularly useful for is in the Emulating private methods with closures section of the Closures article.

#### Recursive functions
JavaScript allows you to call functions recursively. This is particularly useful for dealing with tree structures, such as the those found in the browser DOM.
```JavaScript
function countChars(elm) {
    if (elm.nodeType == 3) { // TEXT_NODE
        reutnr elm.nodeValue.length;
    }
    var count = 0;
    for (var i = 0, child; child = elm.childNodes[i]; i++) {
        count += countChars(child);
    }
    return count;
}
```
This highlights a potential problem with anonymous functions: how do you call them recursively if they don't have a name? JavaScript lets you name function expressions for this. You can use named OOFEs (Immediately Invoked Function Expressions) as shown below:
```JavaScript
var charsInBody = (function counter(lem) {
    if (elm.nodeType == 3) { // TEXT_NODE
        return elm.nodeValue.length;
    }
    var count = 0;
    for (var i = 0, cihld; cihld = elm.childNodes[i]; i++) {
        count += counter(child);
    }
    return count;
})(document.body);
```
The name provided to a function expression as above is only available to the function's own scope. This allows more optimizations to be done by the engine and results in more readable code. The name also shows up in the debugger and some stack traces, which can save you time when debugging.

Note that JavaScript functions are themselves objects - like everything else in JavaScript - and you can add or change properties on them just like we've seen earlier in the Objects section.

### Custom objects

#### Inner functions
JavaScript function declarations are allowed inside other functions. We've seen this once before, with an earlier `makePerson()` function. An important detail of nested functions in JavaScript is that they can access variables in their parent function's scope:
```JavaScript
function parentFunc() {
    var a = 1;
    
    function nestedFunc() {
        var b = 4; // parentFunc can't use this
        return a + b;
    }
    return nestedFunc(); // 5
}
```
This provides a great deal of utility in writing more maintainable code. If a called function relies on one or two other functions that are not useful to any other part of your code, you can nest those utility functions inside it. This keeps the number of functions that are in the global scope down, which is always a good thing.

This is also great counter to the lure of global variables. When writing complex code it is often tempting to use global variables to share values between multiple functions - which leads to code that is hard to maintain. Nested functions can share variables in their parent, so you can use that mechanism to couple functions together when it makes sense without polluting your global namespace - "local globals" if you like. This technique should be used with caution, but it's a useful ability to have.

### Closures

----------

## Glossary

### Falsy | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
A falsy (sometimes written falsey) value is a value that is considered false when encountered in a Boolean context.

JavaScript uses type conversion to coerce any value to a Boolean in contexts that require it, such as conditionals and loops.

The following table provides a complete list of JavaScript falsy values:

|Value|Description|
|:----|:----------|
|false|The keyword false.|
|0|The Number zero(so, also 0.0, etc., and 0x0).|
|-0|The Number negative zero (so, also -0.0, etc., and -0x0).|
|0n|The BigInt zero (so, also 0x0n). Note that there is no BigInt negative zero - the negation of 0n is 0n.|
|" ", ' ', ` `|Empty string value.|
|null|null-the absence of any value.|
|undefined|undefined - the primitive value.|
|NaN|NaN - not a number.|
|document.all|Objects are falsy if and only if they have the IsHTMLDDA internal slot. That slot only exists in document.all and cannot be set using JavaScript.|

```JavaScript
// Examples of falsy values in JavaScript (which are coerced to false in Boolean contexts, and thus bypass the if block):
if (false)
if (null)
if (undefined)
if (0)
if (-0)
if (0n)
if (NaN)
if ("")
```

#### The logical AND operator, &&
If the first object is falsy, it returns that object
```JavaScript
false && "dog" // false
0 && "dog"     // 0
```

### Object | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Object) | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object)
Object refers to a data structure containing data and instructions for working with the data. Objects sometimes refer to real-world things, for example a car or map object in a racing game. JavaScript, Java, C++, Python, and Ruby are examples of object-oriented programming languages.

The `Object` class represents one of JavaScript's data types. It is used to store various keyed collections and more complex entities. Objects can be created using the `Object()` constructor or the object initializer/literal syntax.

### Object.entires() | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries)
The `Object.entries()` method returns an array of a given object's own enumerable string-keyed property [key, value] pairs. This is the same as iterating with a `for...in` loop, except that a `for...in` loop enumerates properties in the prototype chain as well.

### Primitive | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
In JavaScript, a primitive (primitive value, primitive data type) is data that is not an object and has no methods. There are 7 primitive data types: string, number, bigint, boolean, undefined, symbol, and null.

Most of the time, a primitive value is represented directly at the lowest level of the language implementation.

All primitive are immutable, i.e., they cannot be altered. It is important not to confuse a primitive itself with a variabel assigned a primitive value. The variable may be reassigned a new value, but the existing value can not be changed in the ways that objects, arrays, and functions can be altered.

### Property | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/property)
The term property can have several meanings depending on the context. It may refer to:

Property (CSS): A CSS property is a characteristic (like color) whose associated value defines one aspect of how the browser should display the element.

Property (JavaScript): A JavaScript property is a characteristic of an object, often describing attributes associated with a data structure.

### Truthy | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
In JavaScript, a truthy value is a value that is considered true when encountered in a Boolean context. All values are truthy unless they are defined as falsy. (i.e., except for false, 0, -0, 0n, "", null, undefined, and NaN).

JavaScript uses type coercion in Boolean contexts.

```JavaScript
// Examples of truthy values in JavaScript (which will be coerced to tru in boolean contexts, and thus execute the if block):
if (true)
if ({})
if ([])
if (42)
if ("0")
if ("false")
if (new Data())
if (-42)
if (12n)
if (3.14)
if (-3.14)
if (Infinity)
if (-Infinity)
```

#### The logical AND operator, &&
If the first object is truthy, the logical AND operator returns the second operand:
```JavaScript
true && "dog" // "dog"
[] && "dog"   // "dog"
```

### Type Conversion | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Type_Conversion)
Type conversion (or typecasting) means transfer of data from one data type to another. Implicit conversion happens when the compiler automatically assigns data types, but the source code can also explicitly require a conversion to take place. For example, given the instruction 5+2.0, the floating point 2.0 is implicitly typecasted into an integer, but given the instruction Number("0x11"), the string "0x11" is explicitly typecasted as the number 17.

### Type Coercion | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion)
Type coercion is the automatic or implicit conversion of values from one data type to another (such as strings to numbers). Type conversion is similar to type coercion because they both convert values from one data type to another with one key difference - type coercion is implicit whereas type conversion can be either implicit or explicit.

```JavaScript
const value1 = '5';
const value9 = 9;
let sum = value1 + value2; // 9 -> '9'
console.log(sum);          // '59'
// JavaScript had a choice between a string or a number and decided to use a string.
```

### Value | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Value)
In the context of data or an object wrapper around that data, the value is the primitive value that the object wrapper contains. In the context of a variable or property, the value can be either a primitive or an object reference.

### Variable | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Variable)
A variable is a named reference to a value. That way an unpredictable value can be accessed through a predetermined name.

----------

## Statements

### Arrow function expressions | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
An arrow function expression is a compact alternative to a tranditional function expression, but is limited and can't be used in all situations.

Differences & Limitations:

- Does not have its own bindings to `this` or `super`, and should not be used as methods.
- Does not have `new.target` keyword.
- Not suitable for call, apply and bind methods, which generally rely on establishing a scope.
- Can not be used as constructors.
- Can not use yield, within its body.

### var | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
The `var` statement declares a function-scoped or globally-scoped variable, optionally initializing it to a value.

### let | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
The `let` statement declares a block-scoped local variable, optionally initializing it to a value.

----------

# JavaScript Tutorial | [w3schools](https://www.w3schools.com/js/default.asp)
JavaScript is the world's most popular programming language, the programming language or the Web, and easy to learn.
JavaScript is one of the 3 languages all web developers must learn: HTML to define the content of web pages, CSS to specify the layout of web pages, and JavaScript to program the behavior of web pages.

----------

### Hoisting | [MDN (KR)](https://developer.mozilla.org/ko/docs/Glossary/Hoisting)
호이스팅이랑 인터프리터가 변수와 함수의 메모리 공간 선언 전에 미리 할당하는 것을 의미합니다. var로 선언한 변수의 경우 호이스팅 시 undefined로 변수를 초기화합니다. 반면 let과 const로 선언한 변수의 경우 호이스팅 시 변수를 초기화하지 않습니다. 따라서 변수를 정의하는 코드보다 사용하는 코드가 앞서 등장할 수 있습니다. 다만 선언와 초기화를 함께 수행하는 경우, 선언 코드까지 실행해야 변수가 초기화된 상태가 됨을 주의하세요.

### Arrow Function | [MDN (KR)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
화살표 함수 표현(arrow function expression)은 전통적인 함수표현(function)의 간편한 대안입니다. 하지만, 화살표 함수는 몇 가지 제한점이 있고 모든 상황에 사용할 수는 없습니다.

- this나 super에 대한 바인딩이 없고, methods로 사용될 수 없습니다.
- new.target 키워드가 없습니다.
- 일반적으로 스코프를 지정할 때 사용하는 call, apply, bind methods를 이용할 수 없습니다.
- 생성자(Constructor)로 사용할 수 없습니다.
- yield를 화살표 함수 내부에서 사용할 수 없습니다.

```JavaScript
(param1, param2, ..., paramN) => { statements }
(param1, param2, ..., paramN) => expression
// 다음과 동일함: => { return expression; }

// 매개변수가 하나뿐인 경우 괄호는 선택사항:
(singleParam) => { statements }
singleParam => { statements }

// 매개변수가 없는 함수는 괄호가 필요:
() => { statements }

// 객체 리터럴 표현을 반환하기 위해서는 함수 본문(body)을 괄호 속에 넣음:
params => ({foo: bar})

// 나머지 매개변수 및 기본 매개변수를 지원함
(param1, param2, ...rest) => { statements }
(param1 = defaultValue1, param2, ..., paramN = defaultValueN) => { statements }

// 매개변수 목록 내 구조분해할당도 지원됨
var f = ([a, b] = [1, 2], {x: c} = {x: a + b}) => a + b + c;
f(); // 6
```
화살표 함수 도입에 영향을 준 두 요소: 보다 짧아진 함수 및 바인딩하지 않은 this.

```JavaScript
var elements = [
  'Hydrogen',
  'Helium',
  'Lithium',
  'Beryllium',
];

// 이 문장은 배열을 반환함: [8, 6, 7, 9]
elements.map(function(element) {
  return element.length;
});

// 위의 일반적인 함수 표현은 아래 화살표 함수로 쓸 수 있다.
elements.map((element) => {
  return element.length;
}); // [8, 6, 7, 9]

// 파라미터가 하나만 있을 때는 주변 괄호를 생략할 수 있다.
elements.map(element => {
  return element.length;
}); // [8, 6, 7, 9]

// 화살표 함수의 유일한 문장이 'return'일 때 'return'과
// 중괄호({})를 생략할 수 있다.
elements.map(element => element.length); // [8, 6, 7, 9]

// 이 경우 length 속성만 필요하므로 destructuring 매개변수를 사용할 수 있다.
// 'length'는 우리가 얻고자 하는 속성에 해당하는 반면,
// lengthFooBarX'는 변경 가능한 변수의 이름일 뿐이므로
// 원하는 유효한 변수명으로 변경할 수 있다.
elements.map(({ length: lengthFooBarX }) => lengthFooBarX); // [8, 6, 7, 9]

// destructuring 파라미터 할당도 아래와 같이 작성할 수 있습니다.
// 이 예에서 정의한 객체 내의 'length'에 값을 지정하지 않은 점에 주목하세요. 대신, "length" 변수의
// 리터럴 이름은 우리가 해당 객체에서 꺼내오고 싶은 속성 이름 자체로 사용됩니다.
elements.map(({ length }) => length); // [8, 6, 7, 9]
```

#### 바인딩 되지 않은 this

화살표 함수가 나오기 전까지는, 모든 새로운 함수는, 어떻게 그 함수가 호출되는지에 따라 자신의 this 값을 정의했습니다:

- 이 함수가 생성자인 경우는 새로운 객체
- 엄격 모드 함수 호출에서는 undefined
- 함수가 "객체 메서드"로서 호출된 경우 문맥 객체
- 등등

이는 객체 지향 스타일로 프로그래밍할 때 별로 좋지 않습니다.

#### 바인딩 되지 않은 arguments

화살표 함수는 arguments 객체를 바인드 하지 않습니다. 때문에, arguments는 그저 둘러싸는 범위(scope) 내 이름에 대한 참조입니다.

화살표 함수는 자신의 arguments 객체가 없지만, 대부분의 경우에 나머지 매개변수가 좋은 대안입니다:

#### 메소드로 사용되는 화살표 함수

이야기 했듯이, 화살표 함수 표현은 메소드 함수가 아닌 형태로 사용 할 수 있습니다. 메소드로 사용하려고 한면 무슨일이 발생하는지 봅시다.

#### new 연산자 사용

화살표 함수는 생성자로서 사용될 수 없으며 new와 함께 사용하면 오류가 발생합니다.

#### prototype 속성 사용

화살표 함수는 prototype 속성이 없습니다.

#### yield 키워드 사용

yield 키워드는 화살표 함수의 본문(그 안에 더 중첩된 함수 내에서 허용한 경우를 제외하고)에 사용될 수 없습니다. 그 결과, 화살표 함수는 생성기(generator)로서 사용될 수 없습니다.

### Rest Parameter | [MDN (KR)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/rest_parameters)
나머지 매개변수 구문을 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받을 수 있습니다.

```JavaScript
function f(a, b, ...theArgs) {
  // ...
}
```

함수의 마지막 매개변수 앞에 "..."(세 개의 U+002E FULL STOP 문자)를 붙이면 (사용자가 제공한) 모든 후속 매개변수를 표준 JavaScript 배열에 넣도록 지정합니다. 마지막 매개변수만 나머지 매개변수로 설정할 수 있습니다.

함수 정의에는 하나의 ...만 존재할 수 있습니다. 나머지 매개변수는 반드시 함수 정의의 마지막 매개변수여야 합니다.

```JavaScript
foo(...one, ...wrong, ...wrong) // X
foo(...wrong, arg2, arg3)       // X
foo(arg1, arg2, ...correct)     // O
```

#### 나머지 매개변수와 arguments 객체의 차이
나머지 매개변수와 arguments 객체 사이에는 세 개의 주요 차이가 있습니다.

- arguments 객체는 실제 배열이 아닙니다. 그러나 나머지 매개변수는 Array 인스턴스이므로 sort, map, forEach, pop 등의 메서드를 직접 적용할 수 있습니다.
- arguments 객체는 callee 속성과 같은 추가 기능을 포함합니다.
- ...restParam은 후속 매개변수만 배열에 포함하므로 ...restParam 이전에 직접 정의한 매개변수는 포함하지 않습니다. 그러나 arguments 객체는, ...restParam의 각 항목까지 더해 모든 매개변수를 포함합니다.

#### 인수에서 배열로

나머지 매개변수는 다수의 인수를 배열로 변환하는 과정의 보일러플레이트 코드를 줄이기 위해 도입됐습니다.

```JavaScript
// 나머지 매개변수 이전에 "arguments"를 일반 배열로 변환하던 방법
function f(a, b) {
  let normalArray = Array.prototype.slice.call(arguments)
  // -- 또는 --
  let normalArray = [].slice.call(arguments)
  // -- 또는 --
  let normalArray = Array.from(arguments)
  
  let first = normalArray.shift() // 동작, 첫 번째 매개변수 반환
  let first = arguments.shift()   // 오류, arguments는 실제 배열이 아님
}
```

### Default Parameter | [MDN (KR)](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Default_parameters)
기본값 함수 매개변수(default function parameter)를 사용하면 값이 없거나 undefined가 전달될 경우 이름붙은 매개변수를 기본값으로 초기화할 수 있습니다. 

```JavaScript
function fnName(param1 = defaultValue1, ..., paramN = defaultValueN) { ... }
```

JavaScript에서, 함수의 매개변수는 undefined가 기본입니다. 그러나, 일부 상황에서는 다른 기본 값을 설정하는 것이 유용할 수 있습니다. 이때가 바로 기본값 매개변수가 필요할 때 입니다.

과거에 기본값 설정을 위한 일반적인 방법은 함수 내부(body)에서 매개변수 값을 검사해 undefined인 경우 값을 할당하는 것이었습니다.

다음 예제에서, multiply 호출 시 b에 할당된 값이 없다면, b 값은 a * b를 평가할 때 undefined일 거고 multiply 호출은 NaN이 반환됩니다.

```JavaScript
function multiply(a, b) {
  return a * b
}

multiply(5, 2) // 10
multiply(5)    // NaN!
```

이를 방지하기 위해서, 아래 두 번째 줄과 같이 multiply 함수가 오직 한 개의 인수만 있다면 b를 1로 설정하는 방식을 사용하곤 했습니다.

```JavaScript
function multiply(a, b) {
  b = (typeof b !== 'undefined') ? b : 1
  return a * b
}

multiply(5, 2) // 10
multiply(5)    // 5
```

ES2015의 기본값 매개변수로 함수 내부에서의 검사는 더 이상 필요치 않습니다. 이제, 간단히 함수 머리(head)에서 b의 기본값으로 1로 설정할 수 있습니다:

```JavaScript
function multiply(a, b = 1) {
  return a * b
}

multiply(5, 2)         // 10
multiply(5)            // 5
multiply(5, undefined) // 5
```

#### undefined vs. 다른 거짓같은 값(falsy values) 전달하기
아래 예제 중 두 번째 호출에서, 설사 두 번째 인수를 호출할 때 명시해서 undefined(null 혹은 falsy 값이 아니긴 하지만)로 설정하더라도, num 인수의 값은 여전히 기본값입니다.

### for-in vs. for-of | [Blog (KR)](https://jsdev.kr/t/for-in-vs-for-of/2938)
for-in은 object의 모든 열거 가능한 속성에 대해 반복이 가능하지만, for-of는 [Symbol.iterator] 속성을 가지는 collection만 사용할 수 있다.

### Closure vs. Callback | [Stackoverflow](https://stackoverflow.com/questions/615907/how-is-a-closure-different-from-a-callback) | [Blog (KR)](https://poiemaweb.com/js-closure)
Callback은 function pointer와 같이 사용되고 Closure는 function과 function 선언되었을 때 (declared) context (lexical environment)의 조합이다.

### Closure | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function's scope from an inner function. In JavaScript, closures are created every time a function is created, at function creation time.

----------

#### Reference
- JavaScript, https://developer.mozilla.org/en-US/docs/Glossary/JavaScript, 2021-06-23-Wed.
- JavaScript basics, https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics, 2021-06-22-Tue.
- JavaScript Tutorial, https://www.w3schools.com/js/default.asp, 2021-06-23-Wed.
- Falsy MDN, https://developer.mozilla.org/en-US/docs/Glossary/Falsy, 2021-12-09-Thu.
- Object, https://developer.mozilla.org/en-US/docs/Glossary/Object, 2021-06-24-Thu.
- Primitive, https://developer.mozilla.org/en-US/docs/Glossary/Primitive, 2021-06-24-Thu.
- Property, https://developer.mozilla.org/en-US/docs/Glossary/property, 2021-06-24-Thu.
- Truthy MDN, https://developer.mozilla.org/en-US/docs/Glossary/Truthy, 2021-12-09-Thu.
- Type Conversion MDN, https://developer.mozilla.org/en-US/docs/Glossary/Type_Conversion, 2021-12-09-Thu.
- Type Coercion MDN, https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion, 2021-12-09-Thu.
- Value, https://developer.mozilla.org/en-US/docs/Glossary/Value, 2021-06-24-Thu.
- Variable, https://developer.mozilla.org/en-US/docs/Glossary/Variable, 2021-06-24-Thu.
- var, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var, 2021-06-24-Thu.
- let, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let, 2021-06-24-Thu.
- Semicolon guide, https://news.codecademy.com/your-guide-to-semicolons-in-javascript/, 2021-06-24-Thu.
- naming rules, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables, 2021-06-24-Thu.
- checking your varibale name, https://mothereff.in/js-variables, 2021-06-24-Thu.
- The difference between var and let, https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables#the_difference_between_var_and_let, 2021-06-24-Thu.
- A re-introduction to JavaScript (JS tutorial), https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript, 2021-07-01-Thu.
- Object MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object, 2021-09-17-Fri.
- Object.entries() MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries, 2021-09-17-Fri.
- Arrow function expressions MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions 2021-09-17-Fri.
- Data Types and Data Structures MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures, 2021-10-01-Fri.
- Boolean MDN, https://developer.mozilla.org/en-US/docs/Glossary/Boolean, 2021-10-01-Fri.
- Boolean MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean, 2021-10-01-Fri.
- Null MDN, https://developer.mozilla.org/en-US/docs/Glossary/Null, 2021-10-01-Fri.
- Null MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/null, 2021-10-01-Fri.
- Undefined MDN, https://developer.mozilla.org/en-US/docs/Glossary/undefined, 2021-10-01-Fri.
- Undefined MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined, 2021-10-01-Fri.
- Symbol MDN, https://developer.mozilla.org/en-US/docs/Glossary/Symbol, 2021-10-01-Fri.
- Symbol MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol, 2021-10-01-Fri.
- Map MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map, 2021-10-05-Tue.
- Symbol MDN, https://developer.mozilla.org/en-US/docs/Glossary/Symbol, 2021-10-05-Tue.
- Object.entires() MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries, 2021-10-06-Wed.
- Hoisting MDN KR, https://developer.mozilla.org/ko/docs/Glossary/Hoisting, 2021-12-09-Thu.
- Arrow Function MDN KR, https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Arrow_functions, 2021-12-09-Thu.
- Rest Parameter MDN KR, https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/rest_parameters, 2021-12-09-Thu.
- Default Parameter MDN KR, https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Default_parameters, 2021-12-09-Thu.
- for-in vs. for-of Blog KR, https://jsdev.kr/t/for-in-vs-for-of/2938, 2022-01-07-Fri.
- Closure vs. Callback Stackoverflow, https://stackoverflow.com/questions/615907/how-is-a-closure-different-from-a-callback, 2022-01-07-Fri.
- Closure Blog KR, https://poiemaweb.com/js-closure, 2022-01-07-Fri.
- Closuer MDN, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures, 2022-01-07-Fri.

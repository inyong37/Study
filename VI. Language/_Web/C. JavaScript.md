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

### Object | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Object)
Object refers to a data structure containing data and instructions for working with the data. Objects sometimes refer to real-world things, for example a car or map object in a racing game. JavaScript, Java, C++, Python, and Ruby are examples of object-oriented programming languages.

### Primitive | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
In JavaScript, a primitive (primitive value, primitive data type) is data that is not an object and has no methods. There are 7 primitive data types: string, number, bigint, boolean, undefined, symbol, and null.

Most of the time, a primitive value is represented directly at the lowest level of the language implementation.

All primitive are immutable, i.e., they cannot be altered. It is important not to confuse a primitive itself with a variabel assigned a primitive value. The variable may be reassigned a new value, but the existing value can not be changed in the ways that objects, arrays, and functions can be altered.

### Property | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/property)
The term property can have several meanings depending on the context. It may refer to:

Property (CSS): A CSS property is a characteristic (like color) whose associated value defines one aspect of how the browser should display the element.

Property (JavaScript): A JavaScript property is a characteristic of an object, often describing attributes associated with a data structure.


### Value | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Value)
In the context of data or an object wrapper around that data, the value is the primitive value that the object wrapper contains. In the context of a variable or property, the value can be either a primitive or an object reference.

### Variable | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Variable)
A variable is a named reference to a value. That way an unpredictable value can be accessed through a predetermined name.

----------

## Statements

### var | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var)
The `var` statement declares a function-scoped or globally-scoped variable, optionally initializing it to a value.

### let | [MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
The `let` statement declares a block-scoped local variable, optionally initializing it to a value.

----------

# JavaScript Tutorial | [w3schools](https://www.w3schools.com/js/default.asp)
JavaScript is the world's most popular programming language, the programming language or the Web, and easy to learn.
JavaScript is one of the 3 languages all web developers must learn: HTML to define the content of web pages, CSS to specify the layout of web pages, and JavaScript to program the behavior of web pages.

----------

#### Reference
- JavaScript, https://developer.mozilla.org/en-US/docs/Glossary/JavaScript, 2021-06-23-Wed.
- JavaScript basics, https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics, 2021-06-22-Tue.
- JavaScript Tutorial, https://www.w3schools.com/js/default.asp, 2021-06-23-Wed.
- Object, https://developer.mozilla.org/en-US/docs/Glossary/Object, 2021-06-24-Thu.
- Primitive, https://developer.mozilla.org/en-US/docs/Glossary/Primitive, 2021-06-24-Thu.
- Property, https://developer.mozilla.org/en-US/docs/Glossary/property, 2021-06-24-Thu.
- Value, https://developer.mozilla.org/en-US/docs/Glossary/Value, 2021-06-24-Thu.
- Variable, https://developer.mozilla.org/en-US/docs/Glossary/Variable, 2021-06-24-Thu.
- var, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var, 2021-06-24-Thu.
- let, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let, 2021-06-24-Thu.
- Semicolon guide, https://news.codecademy.com/your-guide-to-semicolons-in-javascript/, 2021-06-24-Thu.
- naming rules, https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#variables, 2021-06-24-Thu.
- checking your varibale name, https://mothereff.in/js-variables, 2021-06-24-Thu.
- The difference between var and let, https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables#the_difference_between_var_and_let, 2021-06-24-Thu.
- A re-introduction to JavaScript (JS tutorial), https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript, 2021-07-01-Thu.
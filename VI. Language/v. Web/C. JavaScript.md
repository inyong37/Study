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
Comments are snippets of text that can be added along with code. The browser ignores text marked as comments. You can write comments in JavaScript just as you can in CSS. `/* */`. If your commment contains no line breaks, it's an option to put it behind two slashs like this. `//`  

### Operators

### Conditionals

### Functions

### Events

## Supercharging our example website

### Adding an image changer

### Adding a personalized welcome message

### A user name of null?

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

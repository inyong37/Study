# TypeScript | [Homepage](https://www.typescriptlang.org/)
*Typed JavaScript at Any Scale.*

*By understanding JavaScript, TypeScript saves you time catching errors and providing fixes before you run code.*

*Any browser, any OS, anywhere JavaScript runs.*

*Entirely Open Source*

----------

## Data Type | [Docs](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html)
In TypeScript, it supports the same types as in JavaScript, with an extra enumeration type thrown in to help things along.

### Boolean
The most basic datatype is the simple true/false value, which JavaScript and TypeScript call a `boolean` value.

```TypeScript
let isDone: boolean = false;
```

### Number
As in JavaScript, all numbers in TypeScript are either floating point values or BigIntegers. These floating point numbers get the type `number`, while BigIntegers get the type `bigint`. In addition to hexadecimal and decimal literals, TypeScript also supports binary and octal literals introduced in ECMAScript 2015.

```TypeScript
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
let big: bigint = 100n;
```

- Convert String to Number | [stackoverflow](https://stackoverflow.com/questions/14667713/how-to-convert-a-string-to-number-in-typescript?rq=1):

```TypeScript
var x: string = "32";
var y: number = +x;
```

- Check the number is float or integer | [stackoverflow](https://stackoverflow.com/questions/3885817/how-do-i-check-that-a-number-is-float-or-integer/20779354#20779354):
```TypeScript
function isInt(n){
  return Number(n) === n && n % 1 === 0;
}

function isFloat(n){
  return Number(n) === n && n % 1 !== 0;
}
```

### String
Another fundamental part of creating programs in JavaScript for webpages and servers alike is working with textual data. As in other languages, it uses the type `string` to refer to these textual datatypes. Just like JavaScript, TypeScript also uses double quotes (`"`) or single quotes (`'`) to surround string data.

```TypeScript
let color: string = "blue";
color = 'red';
```

It can also uses template strings, which can span multiple lines and have embedded expressions. These strings are surrounded by the backtick/backquote charcter, and embedded expressions are of the form `${ expr }`.

```TypeScript
let fullname: string = `Bob Bobbington`;
let age: number = 37;
let sentence: string = `Hello, my name is ${fullname}.

I'll be ${age + 1} years old next month.`;
```

----------

## Utility Type | [Docs](https://www.typescriptlang.org/docs/handbook/utility-types.html)

### Record<Keys, Type>
Constructs an object type whose property keys are `Keys` and whose property values are `Type`. This utility can be used to map the properties of a type to another type.

```TypeScript
interface  CatInfo {
  age: number;
  breed: string;
}

type CatName = "miffy" | "boris" | "mordred";

const cats: Record<CatName, CatInfo> = {
  miffy: { age: 10, breed: "Persian" },
  boris: { age: 5, breed: "Maine Coon" },
  mordred: { age: 16, breed: "British Shorthair" },
};

cats.boris;
```

----------

#### Reference
- TypeScript, https://www.typescriptlang.org/, 2021-07-01-Thu.
- Data Type Docs (Deprecated), https://www.typescriptlang.org/docs/handbook/basic-types.html, 2021-10-01-Fri.
- Data Type Docs, https://www.typescriptlang.org/docs/handbook/2/everyday-types.html, 2021-10-01-Fri.
- Utility Type Docs, https://www.typescriptlang.org/docs/handbook/utility-types.html, 2021-10-05-Tue.
- Convert String to Number, https://stackoverflow.com/questions/14667713/how-to-convert-a-string-to-number-in-typescript?rq=1, 2021-10-08-Fri.
- Check the number is float or integer, https://stackoverflow.com/questions/3885817/how-do-i-check-that-a-number-is-float-or-integer/20779354#20779354, 2021-10-08-Fri.

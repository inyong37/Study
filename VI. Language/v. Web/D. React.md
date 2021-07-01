# React | [Homepage](https://reactjs.org/)
A JavaScript library for building user interfaces.

## Main Concepts

1.[Hello World](https://reactjs.org/docs/hello-world.html) 

2. [Introducing JSX](https://reactjs.org/docs/introducing-jsx.html)

3. [Rendering Elements](https://reactjs.org/docs/rendering-elements.html)

4. [Components and Props](https://reactjs.org/docs/components-and-props.html)

5. [State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html)

6. [Handling Events](https://reactjs.org/docs/handling-events.html)

7. [Conditional Rendering](https://reactjs.org/docs/conditional-rendering.html)

8. [Lists and Keys](https://reactjs.org/docs/lists-and-keys.html)

9. [Forms](https://reactjs.org/docs/forms.html)

10. [Lifting State Up](https://reactjs.org/docs/lifting-state-up.html)

11. [Composition vs Inheritance](https://reactjs.org/docs/composition-vs-inheritance.html)

12. [Thinking in React](https://reactjs.org/docs/thinking-in-react.html)

## Hooks

1. [Introducing Hooks](https://reactjs.org/docs/hooks-intro.html)

### [Modern JavaScript in React Documentation](https://gist.github.com/gaearon/683e676101005de0add59e8bb345340c)
If you haven’t worked with JavaScript in the last few years, these three points should give you enough knowledge to feel comfortable reading the React documentation:

* We define variables with [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let) and [`const`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/const) statements. For the purposes of the React documentation, you can consider them equivalent to [`var`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/var).
* We use the `class` keyword to define [JavaScript classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes). There are two things worth remembering about them. Firstly, unlike with objects, you *don't* need to put commas between class method definitions. Secondly, unlike many other languages with classes, in JavaScript the value of `this` in a method [depends on how it is called](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes#Boxing_with_prototype_and_static_methods).
* We sometimes use `=>` to define ["arrow functions"](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions). They're like regular functions, but shorter. For example, `x => x * 2` is roughly equivalent to `function(x) { return x * 2; }`. Importantly, arrow functions [don't have their own `this` value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions#No_separate_this) so they're handy when you want to preserve the `this` value from an outer method definition.

**Don't worry if this is too much to take in at once. The [MDN JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript) is a stellar resource, and you can consult it whenever you get confused by something.**

Also, when you feel unsure about what some newer syntax means, you can use the [Babel REPL with the ES2015 preset](http://babeljs.io/repl/#?babili=false&browsers=&build=&builtIns=false&code_lz=MYewdgzgLgBAllApgWwjAvDA2gRgDQwBMBAzALoDcAUKJLACYgCuARgDaL0bxKoB0yAIYAHABQAPDAD4YkgFREAlBSA&debug=false&forceAllTransforms=false&shippedProposals=false&circleciRepo=&evaluate=false&fileSize=false&lineWrap=true&presets=es2015%2Creact%2Cstage-1%2Cstage-2%2Cstage-3&prettier=true&targets=Node-6.12&version=6.26.0&envVersion=) to check what equivalent older syntax it compiles to.

## MobX | [Homepage](https://mobx.js.org/README.html)
Simple, scalable state management.

Installation: `$ npm install --save mobx`

## material-ui | [Homepage](https://material-ui.com/)
React components for faster and easier web development.

Installation: `$ npm install @material-ui/core`

----------

#### Reference
- React, https://reactjs.org/, 2021-06-30-Wed.
- MobX, https://mobx.js.org/README.html, 2021-06-30-Wed.
- material-ui, https://reactjs.org/, 2021-06-30-Wed.
- props, state Blog KR, https://velopert.com/3629, 2021-06-30-Wed.
- component Blog KR, https://hyogeun-android.tistory.com/entry/2-React-Component?category=944659, 2021-06-30-Wed.
- Modern JavaScript in React Documentation, https://gist.github.com/gaearon/683e676101005de0add59e8bb345340c, 2021-06-03-Wed.
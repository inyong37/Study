# React | [Homepage](https://reactjs.org/)
A JavaScript library for building user interfaces.

## Main Concepts

1. [Hello World](https://reactjs.org/docs/hello-world.html) 

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

----------

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

### 3. Rendering Elements | [Docs](https://reactjs.org/docs/rendering-elements.html)
Elements are the smallest building blocks of React apps.

An element describes what you want to see on the screen:
```JavaScript
const element = <h1>Hello, world</h1>;
```
Unlike browser DOM elements, React elements are plain objects, and are cheap to create. React DOM takes care of updating the DOM to match the React elements.

#### Note:
One might confuse elements with a more widely known concept of "components". ELements are what components are "made of".

#### Rendering an Element into the DOM
Let's say there is a `<div>` somewhere in your HTML file:
```HTML
<div id="root></div>
```
We call this a "root" DOM node because everything inside it will be managed by React DOM.

Applications build with just React usually have a single root DOM node. If you are integrating React into an existing app, you may have as many isolated root DOM nodes as you like.

To render a React element into a root DOM node, pass both to ReactDOM.render():
```JavaScript
const element = <h1>Hello, world</h1>;
ReactDOM.render(element, document.getElementById('root'));

It displays "Hello, world" on the page.
```

### 4. Components and Props | [Docs](https://reactjs.org/docs/components-and-props.html)
Components let you split the UI into independent, reusable pieces, and think about each piece in isolation. Conceptually, components are like JavaScript functions. They accept arbitrary inputs (called "props") and return React elements describing what should appear on the screen.

#### Function and Class Components
The simplest way to define a component is to write a JavaScript function:
```JavaScript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}
```
This function is a valid React component because it accepts a single "props" (which stands for properties) object argument with data and returns a React element. We call such components "function components" because thay are literally JavaScript functions.

You can also use an ES6 class to define a component.
```JavaScript
class Welecome extends React.Component {
  render() {
    return <h1>Hello, {this.props.name}</h1>;
  }
}
```
The above two components are equivalent from React's point of view.

#### Rendering a Component
Previously, we only encountered React elements that represent DOM tags:
```JavaScript
const element = <div />;
```
However, elements can also represent user-defined componets:
```JavaScript
const element = <Welcome name="Sara" />;
```
When React sees an element representing a user-defined component, it passes JSX attributes and children to this component as a single object. We call this object "props".

For example, this code renders "Hello, Sara" on the page.
```JavaScript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

const element = <Welcome name="Sara" />;
ReactDOM.render(
  element,
  document.getElementById('root')
);
```
#### Note: Always start component names with a capital letter.
React treats components starting with lowercases letters as DOM tags. For example, `<div />` represents an HTML div tag, but `<Welcome />` represents a component and requires `Welcome` to be in scope.

#### Composing Components
Components can refer to other components in their output. This lets us use the same component abstarction for any level of detail. A button, a form, a dialog, a screen: in React apps, all those are commonly expressed as components.

For example, we can create an `App` component that reners `Welcome` many times:
```JavaScript
function Welcome(props) {
  return <h1>Hello, {props.name}</h1>;
}

function App() {
  return (
    <div>
      <Welcome name="Sara" />
      <Welcome name="Cahal" />
      <Welcome name="Edite" />
    </div>
  );
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);
```

Typically, new React apps have a single `App` component at the very top. However, if you integrate React into an existing app, you might start bottom-up with a small component like `Button` and gradually work your way to the top of the view hierarchy.

#### Extracting Components
For example, consider this `Comment` component:
```JavaScript
function Comment(props) {
  return (
    <div className="Comment">
      <div className="UserInfo">
        <img className="Avatar"
          src={props.author.avatarUrl}
          alt={props.author.name}
        />
        <div className="UserInfo-name">
          {props.author.name}
        </div>
      </div>
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```
It accepts `author` (an object), `text` (a string), and `date` (a date) as props, and describes a comment on a social media website.

This component can be trickly to change because of all the nesting, and it is also hard to reuse individual parts of it. Let's extract a few components from it.

First, we will extract `Avatar`:
```JavaScript
function Avatar(props) {
  return (
    <img className="Avatar"
      src={props.user.avatarUrl}
      alt={props.user.name}
    />
  );
}
```
The `Avatar` doesn't need to know that is being rendered inside a `Comment`. This is why we have given its props a more generic name: `user` rather than `author`.

We recommend naming props from the component's own point of view rather than the context in which it is being used.

We can now simplify `Comment` a tiny bit:
```JavaScript
function Comment(props) {
  return (
    <div className="Comment">
      <div className="UserInfo">
        <Avatar user={props.author} />
        <div className="UserInfo-name">
          {props.author.name}
        </div>
      </div>
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```
Next, we will extract a `UserInfo` component that renders an `Avatar` next to the user's name:
```JavaScript
function UserInfo(props) {
  return (
    <div className="UserInfo">
      <Avatar user={props.user} />
      <div className="UserInfo-name">
        {props.user.name}
      </div>
    </div>
  );
}
```
This lets us simplify `Comment` even further:
```JavaScript
function Comment(props) {
  return (
    <div className="Comment">
      <UserInfo user={props.author} />
      <div className="Comment-text">
        {props.text}
      </div>
      <div className="Comment-date">
        {formatDate(props.date)}
      </div>
    </div>
  );
}
```
Extracting components might seem like grunt work at first, but having a palette of reusable components pays off in larger apps. A good rule of thumb is that if a part of your UI is used several times (`Button`, `Panel`, `Avatar`), or is complex enough on its own (`App`, `FeedStory`, `Comment`), it is a good candidate to be extracted to a seperate component.

#### props are Read-Only
Wheter you declare a component as a function or a class, it must never modify its own props. Consider this `sum` function:
```JavaScript
function sum(a, b) {
  return a + b;
}
```
Such functions are called "pure" because they do not attempt to change their inputs, and always return the same result for the same inputs.

In contract, this function is impure because it changes its own inputs:
```JavaScript
function withdraw(account, amount) {
  account.total -= mount;
}
```
React is pretty flexible but it gas a single strict rule:

**All React components must act like pure functions with respect to their props.**

Of course, application UIs are dynamic and change over time. In the next section, we will introduce a new concept of "state". State allows React components to change their output over time in response to user actions, network responses, and anything else, without violating this rule.
----------

#### Reference
- React, https://reactjs.org/, 2021-06-30-Wed.
- MobX, https://mobx.js.org/README.html, 2021-06-30-Wed.
- material-ui, https://reactjs.org/, 2021-06-30-Wed.
- props, state Blog KR, https://velopert.com/3629, 2021-06-30-Wed.
- component Blog KR, https://hyogeun-android.tistory.com/entry/2-React-Component?category=944659, 2021-06-30-Wed.
- Modern JavaScript in React Documentation, https://gist.github.com/gaearon/683e676101005de0add59e8bb345340c, 2021-06-03-Wed.
- Components and Props, https://reactjs.org/docs/components-and-props.html, 2021-08-20-Fri.
- Rendering Elements, https://reactjs.org/docs/rendering-elements.html, 2021-08-20-Fri.

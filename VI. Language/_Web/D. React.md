# React | [Homepage](https://reactjs.org/)
A JavaScript library for building user interfaces.

## Main Concepts

1. [Hello World](https://reactjs.org/docs/hello-world.html) 

2. [Introducing JSX](https://reactjs.org/docs/introducing-jsx.html)

3. [Rendering Elements](https://reactjs.org/docs/rendering-elements.html)

4. [Components and Props](https://reactjs.org/docs/components-and-props.html)

5. [State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html)

6. [Handling Events](https://reactjs.org/docs/handling-events.html) | [React (KR)](https://ko.reactjs.org/docs/handling-events.html)

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
```
It displays "Hello, world" on the page.

#### Updating the Rendered Element
React elements are immutable. Once you create an element, you can't change its children or attributes. An element is like a single frame in a movie: it represents the UI at a certain point in time.

With our knowledge so far, the only way to update the UI is to create a new element, and pass it to ReactDOM.render().

Consider this ticking clock example:
```JavaScript
function tick() {
  const element = (
    <div>
      <h1>Hello, world!</h1>
      <h2>It is {new Date().toLocaleTimeString()}.</h2>
    </div>
  );
  ReactDOM.render(element, document.getElementById('root'));
}

setInterval(tick, 1000);    
```

It calls ReactDOM.render() every second from a setInterval() callback.

#### Note:
In practice, most React apps only call ReactDOM.render() once.

#### React Only Updates What's Necessary
React DOM compares the element and its children to the previous one, and only applies the DOM updates necessary to bring the DOM to the desired state.

Event through we create an element describing the whole UI tre on every tick, only the text node whose contents have changed gets updated by ReactDOM.

In our experience, thinking about how the UI should look at any given moment, rather than how to change it over time, eliminates a whole class of bugs.

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

6. 이벤트 처리하기 | [React (KR)](https://ko.reactjs.org/docs/handling-events.html)
React 엘리먼트에서 이벤트를 처리하는 방식은 DOM 엘리먼트에서 이벤트를 처리하는 방식과 매우 유사합니다. 몇 가지 문법 차이는 다음과 같습니다.

- React의 이벤트는 소문자 대신 camelCase를 사용합니다.
- JSX를 사용하여 문자열이 아닌 함수로 이벤트 핸들러를 전달합니다.

```HTML
<button
  onClick="activaeLasers()">
  Activate Lasers
</button>
```

```React
<button
  onClick={activateLasers}>
  Activate Lasers
</button>
```
또 다른 차이점으로, React는 false를 반환해도 기본 동작을 방지할 수 없습니다. 반드시 preventDefault를 명시적으로 호출해야 합니다. 예를 들어, 일반 HTML에서 폼을 제출할 때 가지고 있는 기본 동작을 방지하기 위해 다음과 같은 코드를 작성할 수 있습니다.
```HTML
<form
  onsubmit="console.log('You clicked submit.'); return false">
  <button type="submit">
    Submit
  </button>
</form>
```

```React
function Form() {
  function handleSubmit(e) {
    e.preventDefault();
    console.log('You clicked submit.');
  }
  
  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Submit</button>
    </form>
  );
}
```
여기서 e는 합성 이벤트입니다. React는 W3C 명세에 따라 합성 이벤트를 정의하기 때문에 브라우저 호환성에 대해 걱정할 필요가 없습니다. React 이벤트는 브라우저 고유 이벤트와 정확히 동일하게 동작하지는 않습니다.

React를 사용할 때 DOM 엘리먼트가 생성된 후 리스너를 추가하기 위해 addEventListener를 호출할 필요가 없습니다. 대신, 엘리먼트가 처음 렌더링될 때 리스너를 제공하면 됩니다.

루프 내부에서는 이벤트 핸들러에 추가적인 매개변수를 전달하는 것이 일반적입니다. 예를 들어, id가 행의 ID일 경우 다음 코드가 모두 작동합니다.

```React
<button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>
<button onClick={this.deleteRow.bind(this, id)}>Delete Row</button>
```

위 두 줄은 동등하며 각각 화살표 함수와 Function.prototype.bind를 사용합니다.

두 경우 모두 React 이벤트를 나타내는 e인자가 ID 뒤에 두 번째 인자로 전달됩니다. 화살표 함수를 사용하면 명시적으로 인자를 전달해야 하지만 bind를 사용할 경우 추가 인자가 자동으로 전달됩니다.

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
- Handling Event KR, https://ko.reactjs.org/docs/handling-events.html, 2021-12-09-Thu.

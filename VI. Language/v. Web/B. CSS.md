# CSS

# CSS basics | [MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
CSS (Cascading Style Sheets) is the code that styles web content. CSS basics walks through what you need to get started. We'll answer questions like: How do I make text red? How do I make content display at a certain location in the (webpage) layout? How do I decorate my webpage with background images and colors?

## What is CSS?
Like HTML, CSS is not a programming language. It's not a markup language either. CSS is a style sheet language. CSS is what you use to selectively style HTML elements. For example, this CSS selects paragraph text, setting the color to red:
```CSS
p {
  color: red;
}
```

To make the code work, we still need to apply this CSS (above) to your HTML document. Otherwise, the styling won't change the appearance of the HTML.

1. Open your `index.html` file. Paste the following line in the head (between the `<head>` and `</head>` tags):
```HTML
<link href='styles/style.css' rel='stylesheet'>
```
2. Save `index.html` and load it in your browser.

If your paragraph text is red, your CSS is working.

### Anatomy of a CSS ruleset
<p align='center'><img src='https://user-images.githubusercontent.com/20737479/123016045-ba91b100-d404-11eb-9636-8332f6336ae3.png'></p>

THe whole structure is called a ruleset. (The term ruleset is often referred to as just rule.) Note the names of the individual parts:

- Selector: This is the HTML element name at the start of the ruleset. It defines the element(s) to be styled (in this example, `<p>` elements). To style a different element, change the selector.
- Declaration: This is a single rule like `color: red;`. It specifies which of the element's properties you want to style.
- Properties: These are ways in which you can style an HTML element. (In this example, `color` is a property of the `<p>` elements.) In CSS, you choose which properties you want to affect in the rule.
- Property value: To the right property - after the colon - there is the property value. This chooses one out of many possible appearances for a given property. (For example, there are many `color` values in addition to `red`.)

Note the other important parts of the syntax:
- Apart from the selector, each ruleset must be wrapped in curly braces. (`{}`)
- Within each declaration, you mush use a colon (`:`) to separate the property from its value or values.
- Within each ruleset, you must use a semicolon (`;`) to separate each declaration from the next one.

To modify multiple property values oin one ruleset, write them separated by semicolons, like this:
```CSS
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```

### Selecting multiple elements
You can also select multiple elements and apply a single ruleset to all of them. Separate multiple selectors by commas. For example:
```CSS
p, li, h1 {
  color: red;
}
```

### Different types of selectors
There are many different types of selectors. The examples above use element selectors, which select all elements of a given type. But we can make more specific selections as well. Here are some of the more common types of selectors:
|Selector name|What does it select|Example|
|:------------|:------------------|:------|
|Element selector (sometimes called a tag or type selector)|All HTML elements of the sepcified type.|`p`<br/>`selects <p>`|
|ID selector|The element on the page with the</br>specified ID. On a given HTML page, each</br>id value should be unique.|`#my-id`</br>`selects <p id='my-id'> or <a id='my-id'>`|
|Class selector|The element(s) on the page with the</br>specified class. Multiple instances of the</br>same class can appear on a page.|`.my-class`</br>`selects <p class='my-class'> and <a class='my-class'>`|
|Attribute selector|The element(s) on the page with the specified attribute.|`img[src]`</br>`selects <img src='myimage.png'> but not <img>`|
|Pseudo-class selector|The specified element(s), but only when in the specified state. (For example, when a cursor hovers over a link.)|`a:hover`</br>`selects <a>, but only when the mouse pointer is hovering over the link.`|

There are many more selectors to discover. :point_right: [CSS selectors](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors)

## Fonts and text

## CSS: all about boxes

### Changing the page color

### Styling the body

### Positioning and styling the main page title

### Centering the image

----------

#### Reference
- CSS basics, https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics, 2021-06-22-Tue.
- CSS selectors, https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors, 2021-06-23-Wed.

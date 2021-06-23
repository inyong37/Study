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

### Different types of selectors

## Fonts and text

## CSS: all about boxes

### Changing the page color

### Styling the body

### Positioning and styling the main page title

### Centering the image

----------

#### Reference
- CSS basics, https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics, 2021-06-22-Tue.

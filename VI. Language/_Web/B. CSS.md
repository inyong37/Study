# CSS: Cascading Style Sheets | [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS)
Cascading Style Sheets (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML (including XML dialects such as SVG, MathML or XHTML). CSS describes how elements should be rendered on screen, on paper, in speech, or on other media.

# CSS Basics | [MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)
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
Now that we've explored some CSS fundamentals, let's improve the appearance of the example by adding more rules and information to the `style.css` file.

1. First, find the output from Google Fonts that you previously saved from [What will your website look like?](). Add the `<link>` element somewhere inside your `index.html`'s head (anywhere between the `<head>` and `</head>` tags). It looks something like this:
```HTML
<link href='https://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet'>
```

This code links your page to a style sheet that loads the Open Sans font family with your webpage.
2. Next, delete the existing rule you have in your `style.css` file. Is was a good test, but let's not continue with lots of red text.
3. Add the following lines (shown below), replacing the `font-family` assignment with your `font-fmaily` selection from [What will your website look like?](). The property `font-family` refers to the font(s) you want to use for text. This rule defines a global base font and font size for the whole page. Since `<html>` is the parent element of the whole page, all element inside it inherit the same `font-size` and `font-family`.
```CSS
html {
  font-size: 10px; /* px mean "pixels": the base font size is now 10p pixels high */
  font-family: "Open Sans", sans-serif; /* this should be the rest of the output you got from Google fonts */
}
```

Note: Anything in CSS between `/*` and `*/` is a CSS comment. The browser ignores comments as it render the code. CSS comments are a way for you to write helpful notes about your code or logic.

4. Now let's set font size for elements that will have text inside the HTML body (`<h1>`, `<li>`, and `<p>`). We'll also center the heading. Finally, let's expand the second ruleset (below) with settings for line height and letter spacing to make body content more readable.
```CSS
h1 {
  font-size: 60px;
  text-align: center;
}

p, li {
  font-size: 16px;
  line-height: 2;
  letter-spacing: 1px;
}
```

## CSS: all about boxes
Something you'll notice about writing CSS: a lot of it is about boxes. This includes setting size, color, and position. Most HTML elements on your page can be thought of as boxes sitting on top of other boxes.

CSS layout is mostly based on the box model. Each box taking up space on your page has properties like:
- `padding`, the space around the content. In the example below, it is the space around the paragraph text.
- `border`, the solid line that is just outside the padding.
- `margin`, the space around the outside of the border.

<p align='center'><img src='https://user-images.githubusercontent.com/20737479/123023273-144ca800-d412-11eb-9adc-be897cc71cac.png'></p>

In this section we also use:
- `width` (of an element).
- `background-color`, the color behind an element's content and padding.
- `color`, the color of an element's content (usually text).
- `text-shadow` sets a drop shadow on the text inside an element.
- `display` sets the display mode of an element. (keep reading to learn more)

To continue, let's add more CSS. Keep adding these new rules at the bottom of `style.css`. Experiment with changing values to see what happens.

### Changing the page color
```CSS
html {
  background-color: #00539F;
}

This rule sets a background color for the entire page. Change the color code to [the color you chose in What will my website look like?]().
```

### Styling the body
```CSS
body{
  width: 600px;
  margin: 0 auto;
  background-color: #FF9500;
  padding: 0 20px 20px 20px;
  border: 5px solid black;
}
```

There are several declarations for the `<body>` element. Let's go through these line-by-line:
- `width: 600px;` This forces the body to always be 600 pixels wide.
- `margin: 0 auto;` When you set two values on a property like `margin` or `padding`,  the first value affects the element's top and bottom side (setting it to `0` in this case); the second value affects the left and right side. (Here, `auto` is a special value that divides the available horizontal space evenly between left and right). You can also use one, three, or four values, as documented in Margin Syntax.
- `background-color: #FF9500;` This sets the element's background color. This project uses a reddish orange for the body background color, as opposed to dark blue for the `<html>` element. (Feel free to experiment.)
- `padding: 0 20px 20px 20px;` This sets four value for padding. The goal is to put some space around the content. In this example, there is no padding on the top of the body, and 20 pixels on the right, bottom, and left. THe values set top, right bottom, left, in that order. As with `margin`, you can use one, two, three, or four values, as documented in Padding Syntax.
- `border: 5px solid black;` This sets values for the width, style and color of the border. In this case, it's a five-pixel-wide, solid black border, on all sides of the body.

### Positioning and styling the main page title
```CSS
h1 {
  margin: 0;
  padding: 20px 0;
  color: #00539F;
  text-shadow: 3px 3px 1px black;
}
```

You may have noticed there's a horrible gap at the top of the body. That happens because browsers apply default styling to the `<h1>` element (among others). That might seem like a bad idea, but the intent is to provide basic readability for unstyled pages. To eliminate the gap, we overwrite the browser's default styling with the setting `margin: 0;`.

Next, we set the heading's top and botton padding to 20 pixels.

Following that, we set the heading text to be the same color as the HTML background color.

Finally, `text-shadow` applies a shadow to the text content of the element. Its four values are:
- The first pixel value sets the horizontal offset of the shadow from the text: how far it moves across.
- The second pixel value sets the vertical offset of the shadow from the text: how far it moves down.
- The third pixel value sets the blur radius of the shaodow. A larger value produces a more fuzzy-looking shadow.
- The fourth value sets the base color of the shadow.

### Centering the image
```CSS
img {
  display: block;
  margin: 0 auto;
}
```
Next, we center the image to make it look better. We could use the `margin: 0 auto` trick again as we did for the body. But there are differences that require an additional setting to make the CSS work.

The `<body>` is a block element, meaning it takes up space on the page. A block elemment can have margin and other spacing values applied to it. In contrash, images are inline elements. It is not possible to apply margin or spacing values to inline elements. So to apply margins to the image, we must give the image block-level behavior using `display: block;`.

Note: The instructions above assume that you're using an image smaller than the width set on the body. (600 pixels) If your image is larget, it will overflow the body, spilling into the rest of the page. To fix this, you can either: 1) reduce the image width using a graphics editor, or 2) use CSS to size the image by setting the width property on the `<img>` element with a smaller value.

----------

## CSS Data Type | [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Types)
CSS data types define typical values (including keywords and units) accepted by CSS properties and functions. They are a special kind of component value type.

The most commonly-used types are defined in the CSS Values and Units specification. This specification also defines functional notations, which allow for more complex types or processing. Other types are defined in the specifications to which they apply.

### Syntax
In formal CSS syntax, data types are denoted by a keyword placed between the inequality signs "`<`" and "`>`".

### Numeric data types
- `<integer>`: One or more decimal units 0 through 9.
- `<number>`: Real numbers which may also have a fractional component, for example 1 or 1.34.
- `<dimension>`: A number with a unit attached to it, for example 23px or 15em.
- `<percentage>`: A number with a percentage sign attached to it, for example 10%.
- `<ratio>`: A ratio, written with the syntax `<number> / <number>`.
- `<flex>`: A flexible length introduced for CSS Grid Layout, written as a `<dimension>` with the `fr` unitl attached and used for grid track sizing.

### Quantities
- `<length>`: Lengths are a `<dimension>` and refer to distances.
- `<angle>`: Angles are used in properties such as `linear-gradient()` and are a `<dimension>` with one of `deg`, `grad`, `rad`, or `turn` units attached.
- `<time>`: Duration units are a `<dimension>` with an `s` or `ms` unit.
- `<frequency>`: Frequencies are a `<dimension>` with a `Hz` or `kHz` unit attached.
- `<resolution>`: Is a `<dimension>` with a unit identifier of `dpi`, `dpcm`, `dppx`, or `x`.

### Combinations of types
- `<length-percentage>`: A type that can accept a length or a percentage as a value.
- `<frequency-percentage>`: A type that can accept a frequency or a percentage as a value.
- `<angle-percentage>`: A type that can accept an angle or a percentage as a value.
- `<time-percentage>`: A type that can accept a time or a percentage as a value.

### Color
- `<color>`: Specified as a keyword or a numerical color value.
- `<alpha-value>`: Specifies the transparency of a color. May be a `<number>`, in which case 0 is fully transparent and 1 is fully opaque, or a `<percentage>`, in which case 0% is fully transparent and 100% fully opaque.

### Images
- `<image>`: A url reference to an image or a color gradient.
- `<color-stop-list>`: A list of two or more color stops with optional transition information using a color hint
- `<linear-color-stop>`: A `<color>` and a `<length-percentage>` to indicate the color stop for this part
- `<linear-color-hint>`: A `<length-percentage>` to indicate how the color interpolates.
- `<ending-shape>`: Used for radial gradients; can have a keyword value of `circle` or `ellipse`.
- `<size>`: Determines the size of the radial gradient's ending shape. This accepts a value of a keyword or a `<length>` but not a percentage.

### 2D positioning
- `<position>`: Defines the position of an object area. Accepts a keyword value such as `top` or `left`, or a `<length-percentage>`.

----------

## CSS Value and Unit | [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units)
Every CSS declaration includes a property / value pair. Depending on the property, the value can include a single integer or keyword, to a series of keywords and values with or without units. There are a common set of data types -- values and units -- that CSS properties accept.

### Textual data types
- `<custom-ident>`
- Pre-defined keywords as an `<ident>`
- `<string>`
- `url()`

Text data types are either `<string>`, a quoated series of characters, or an `<ident>`, a "CSS Identifier" which is an unquoted string. A `<string>` must be quited with either single or double quotes. CSS Identifiers, listed in the specifications as `<ident>` or `<custom-ident>`, must be unquoted.

#### Pre-defined keyword values

#### CSS-wide values

#### URLs

### Numeric data types

#### Integers

#### Numbers

#### Dimensions

#### Distance units

#### Angle units

#### Time units

#### Frequency units

#### Resolution unit

#### Percentages

#### Mixing percentages and dimensions

#### Special data types (defined in other specs)

#### Color

#### Image

#### Position

#### Functional notation

----------

#### Reference
- CSS, https://developer.mozilla.org/en-US/docs/Web/CSS, 2021-12-14-Tue.
- CSS basics, https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics, 2021-06-22-Tue.
- CSS selectors, https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors, 2021-06-23-Wed.
- CSS data types, https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Types, 2021-12-14-Tue.
- CSS values and units, https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units, 2021-12-14-Tue.

# HTML | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/HTML)
HTML (HyperText Markup Language) is a descriptive language that specifies webpage structure.

----------

# HTML basics | [MDN](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
HTMl (HyperText Markup Language) is the code that is used to structure a web page and its content. For example, content could be structured within a set of paragraphs, a list of bullent points, or using images and data tables. As the title suggests, this article will give you a basic understanding of HTML and its functions.

## So what is HTML?
HTML is a markup language that defines the structure of your content. HTML consists of a series of elements, which you use to enclose, or wrpa, different parts of the content to make it appear a certain way, or act a certain way. The enclosing tags can make a word or image hyperlink to somewhere else, can italicize words, can make the font bigger or smaller, and so on. For example, take the following line of content:
```HTML
My cat is very grumpy
```

If we wanted the line to stand by itself, we could specify that it is a paragraph by enclosing it in paragraph tags:
```HTML
<p>My cat is very grumpy</p>
```

### Anatomy of an HTML element
<p align='center'><img src='https://user-images.githubusercontent.com/20737479/122882548-45c46580-d377-11eb-8314-b46d78e8729a.png'></p>

The main parts of our element are as follows:

1. The opening tag: This consists of the name of the element (in this case, p), wrapped in opening and closing angle brackets. This states where the element begins or starts to take effect - in this case where the paragraph begins.
2. The closing tag: This is the same as the opening tag, except that it includes a forward slash before the element name. This states where the element ends = in this case where the paragraph ends. Failing to add a closing tag is one of the standard beginner errors and can lead to starnge results.
3. The content: This is the content of the element, which in this case, is just text.
4. The element: The opening tag, the closing tag, and the content together comprise the element.

Elements can also have attributes that look like the following:
<p align='center'><img src='https://user-images.githubusercontent.com/20737479/122883478-34c82400-d378-11eb-804a-d8d9b923414d.png'></p>

Attributes contain extra information about the element that you don't want to appear in the actual content. Here, class is the attribute name and editor-note is the attribute value. The class attribute allows you to give the element a non-unique identifier that can be used to target it (and any other elements with the same class value) with style information and other things.

An attribute should always have the following:

1. A space between it and the element name (or the previous attribute, if the element already has one or more attributes).
2. The attribute name followed by an equal sign.
3. The attribute value wrapped by opening and closing quotation marks.

### Nesting elements
You can put elements inside other elements too - this is called nesting. If we wanted to state that our cat is very grumpy, we could wrap the word "very" in a `<strong>` element, which means that the word is to be strongly emphasized:
```HTML
  <p>My cat is <strong>very</strong> grumpy.</p>
```

You do however need to make sure that your elements are prperly nested. In the example above, we opend the `<p>` element first, then the `<strong>` element; therefore, we have to close the `<strong>` element first, then the `<p>` element. The elements have to open and close correctly so that they are clearly inside or outside one another. If they overlap as shown above, then your web broswer will try to make the best guess at what you were trying to say, which can lead to unexpected results.

### Empty elements
Some elements have no content and are called empty elements. Take the `<img>` element that we already have in our HTML page:
```
<img src='images/firefox-icon.png' alt='My test image'>
```

This contains two attributes, but there is no closing `</img>` tag and no inner content. This is because an image element doesn't wrap content to affect it. Its purpose is to embed an image in the HTML page in the place it appears.

### Anatomy of an HTML document
That wraps up the basics of individual HTML elements, but they aren't handy on their own. Now we'll look at how individual elements are combined to form an entire HTML page. Let's revisit the code we put into our `index.html` example:
```HTML
<!DOCTYPE html>
<html>
  <head>
    <meta charset='utf-8'>
    <title>My test page</title>
  </head>
  <body>
    <img src='images/firefox-icon.png' alt='My test image'>
  </body>
</html>
```

Here, we have the following:
- `<!DOCTYPE html>` - doctype. It is a requried preamble. In the mists of time, when HTML was young (around 1991/92), doctypes were meant to act as links to a set of rules that the HTML page had to follow to be considered good HTML, which could mean automatic error checking and other useful things. However these days, they don't do much and are basically jush needed to make sure your document behaves correctly. That's all you need to know for now.
- `<html></html>` - the `<html>` element. This element acts as a container for all the stuff you want to include on the HTML page that isn't the content you are showing t your page's viewers. This include things like keywords and a page description that you want to appear in search results, CSS to style our content, character set declarations, and more.
- `<meta charset='utf-8>` - This element sets the character set your document should use to UTF-8 which includes most characters from the vast majority of written languages. Essentially, it can now handle any textual content you might put on it. There is no reason not to set this and it can help avoid some problems later on.
- `<title></title>` - the `<title>` element. This sets the title of your page, which is the title that appears in the browser tab the page is loaded in. It is also used to describe the page when you bookmark/favorite it.
- `<body></body>` - the `<body>` element. This contains all the content that you want to show to web users when they visit your page, whether that's text, images, vidieos, games, playable audio tracks, or whatever else.

## Images
Let's turn our attention to the `<img>` element again:
```HTML
<img src='images/firefox-icon.png' alt='My test image'>
```

As we said before, it embeds an image into our page ion the position it appears. It does this via the `src`(source) attribute, which contains the path to our image file.

We have alos included an `alt`(alternative) attribute. In this attribute, you specify desrciptive text for users who cannot see the image, possibly because of the following reasons:

1. They are visually impaired. Users with significant visual impairments often use tools called screen readers to read out the alt text to them.
2. Something has gone wrong causing the image not to display. For example, try deliberately changing the path inside your `src` attribute to make it incorrect. If you save and reload the page, you should see something like this in place of the image:
<p align='center'><img src='https://user-images.githubusercontent.com/20737479/122887572-00566700-d37c-11eb-8748-5687dca0e0a5.png'></p>

The keywords for alt text are "descriptive text". The alt text you write should provide the reader with enought information to have a good idea of what the image conveys. In this example, our current text of "My test image" is no good at all. A mush better alternative for our Firefox logo would be "The Firefox logo: a flaming fox surrounding the Earth."

## Marking up text
### Headings
Heading elements allow you to specify that certain parts of your content are headings - or subheadings. In the same way that a book has the main title, chapter titles, and subtitles, an HTML document can too. HTML contains 6 heading levels, `<h1>` - `<h6>`, although you'll commonly only use 3 to 4 at most:
```HTML
<h1>My main title</h1>
<h2>My top level heading</h2>
<h3>My subheading</h3>
<h4>My sub-subheading</h4>
```

### Paragraphs
As expained above, `<p>` elements are for containing paragraphs of text; you'll use these frequently when marking up regular text content:
```HTML
<p>This is a single paragraph</p>
```

### Lists
A lot of the web's content is lists and HTML has special elements for these. Marking up lists always consists of at least 2 elements. The most common list types are ordered and unordered lists:

1. Unordered lists are for lists where the order of the items doesn't matter, such as a shopping list. These are wrapped in a `<ul>` element.
2. Ordered lists are for lists where the order of the items does matter, such as a recipe. These are wrapped in an `<ol>` element.

Each item inside the lists is put inside an `<li>`(list item) element.

For example, if we wanted to turn the part of the following paragraph fragment into a list
```HTML
<p>At Mozilla, we're a global community of technologists, thinkers, and builders working together ... </p>
```

We could modify the markup to this
```HTML
<p>At Mozilla, we're a global community of</p>
<ul>
  <li>technologists</li>
  <li>thinkers</li>
  <li>builders</li>
</ul>
<p>working togther ... </p>
```

## Links
Links are very important - they are what makes the web a web! To add a link, we need to use a simple element - `<a>` - "a" being the short form for "anchor". To make text within your paragraph into a link, follow these steps:
1. Choose some text. We chose the text "Mozilla Manifesto".
2. Wrap the text in an `<a>` element, as shown below:
```HTML
<a>Mozilla Manifesto</a>
```
3. Give the `<a>` element an `href` attribute, as shown below:
```HTML
<a href=''>Mozilla Manifesto</a>
```
4. Fill in the value of this attribute with the web address that you want the link to link to:
```HTML
<a href="https://www.mozilla.org/en-US/about/manifesto/">Mozilla Manifesto</a>
```

You might get unexpected results if you omit the `https://` or `http://` part, called the protocol, at the beginning of the web address. After making a link, click it to make sure it is sending you where you wanted it to. (Hypertext REFerence)

----------

# Glossary

## Element | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Element)
An element is a part of a webpage. In XML and HTML, an element may contain a data item or a chunk of text or an image, or perhaps nothing. A typical element includes an opening tag with some attributes, enclosed text content, and a closing tag.

Elements and tags are not the same things. Tags begin or end an element in source code, whereas elements are part of the DOM, the document model for displaying the page in the browser.

<p align='center'><img src='https://user-images.githubusercontent.com/20737479/122880137-a30ae780-d374-11eb-90ec-ca10337e2309.png'></p>

## Attribute | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Attribute)
An attribute extends an element, changing its behavior or providing metadata.

An attribute always has the form `name="value"` (the attribute's identifier followed by its associated value).

You may see attrivutes without the equals sign or a value. That is a shorthand for providing the empty string in HTML, or the attrivute's name in XML.

```HTML
<input required>
<!-- is the same as ... -->
<input required="">
<!-- or -->
<input required="requried">
```

## Tag | [MDN](https://developer.mozilla.org/en-US/docs/Glossary/Tag)
In HTML, a tag is used for creating an element. The name of an HTML element is the name used in anlge brackets such as `<p>` for paragraph. Note that the end tag's name is preceded by a slash character, `</p>`, and that in empty elements, the end tag is neither required nor allowed. If attributes are not mentioned, default values are used in each case.

----------

#### Reference
- HTML, https://developer.mozilla.org/en-US/docs/Glossary/HTML, 2021-06-22-Tue.
- HTML basics, https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics, 2021-06-22-Tue.
- Element, https://developer.mozilla.org/en-US/docs/Glossary/Element, 2021-06-22-Tue.
- Attribute, https://developer.mozilla.org/en-US/docs/Glossary/Attribute. 2021-06-22-Tue.
- Tag, https://developer.mozilla.org/en-US/docs/Glossary/Tag, 2021-06-22-Tue.

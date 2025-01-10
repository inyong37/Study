from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with placeholder content
template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ content }}</p>
    <nav>
        <a href="/">Home</a> |
        <a href="/page1">Page 1</a> |
        <a href="/page2">Page 2</a> |
        <a href="/page3">Page 3</a> |
        <a href="/page4">Page 4</a> |
        <a href="/page5">Page 5</a> |
        <a href="/page6">Page 6</a>
    </nav>
</body>
</html>
"""

# Routes for each page
@app.route('/')
def home():
    return render_template_string(template, title="Home", content="Welcome to the Home page!")

@app.route('/page1')
def page1():
    return render_template_string(template, title="Page 1", content="Content for Page 1")

@app.route('/page2')
def page2():
    return render_template_string(template, title="Page 2", content="Content for Page 2")

@app.route('/page3')
def page3():
    return render_template_string(template, title="Page 3", content="Content for Page 3")

@app.route('/page4')
def page4():
    return render_template_string(template, title="Page 4", content="Content for Page 4")

@app.route('/page5')
def page5():
    return render_template_string(template, title="Page 5", content="Content for Page 5")

@app.route('/page6')
def page6():
    return render_template_string(template, title="Page 6", content="Content for Page 6")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

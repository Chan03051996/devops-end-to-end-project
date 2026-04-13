<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, request, render_template_string

>>>>>>> 0a37273 (auto deploy test)
app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps App</title>
</head>
<body>
    <h2>🚀 DevOps Project Form</h2>
    
    <form method="POST">
        Name: <input type="text" name="name"><br><br>
        Message: <input type="text" name="message"><br><br>
        <input type="submit" value="Submit">
    </form>

    {% if name %}
        <h3>Hello {{name}} 👋</h3>
        <p>Your message: {{message}}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    message = None

    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

    return render_template_string(html, name=name, message=message)

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=5000)
=======
from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
    <title>DevOps App</title>
</head>
<body>
    <h2>🚀 DevOps Project Form</h2>
    
    <form method="POST">
        Name: <input type="text" name="name"><br><br>
        Message: <input type="text" name="message"><br><br>
        <input type="submit" value="Submit">
    </form>

    {% if name %}
        <h3>Hello {{name}} 👋</h3>
        <p>Your message: {{message}}</p>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    message = None

    if request.method == 'POST':
        name = request.form.get('name')
        message = request.form.get('message')

    return render_template_string(html, name=name, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 26fd54f (Add form UI to app)
=======
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 0a37273 (auto deploy test)

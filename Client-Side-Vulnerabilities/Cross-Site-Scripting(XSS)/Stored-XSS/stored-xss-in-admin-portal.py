from flask import Flask, request, redirect

app = Flask(__name__)
messages = []  # Stores messages globally

@app.route('/', methods=['GET', 'POST'])
def index():
    global messages
    if request.method == 'POST':
        if 'message' in request.form:
            message = request.form['message']
            messages.append(message)  # Store message
        elif 'clear' in request.form:
            messages = []  # Clear all messages
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Stored XSS Tester</title>
    </head>
    <body>
        <h1>Stored XSS Testing App</h1>
        <a href="/">Send Message</a> | <a href="/admin">Admin Portal</a>
        <hr>
        <h2>Send Message</h2>
        <form method="post">
            <textarea name="message" rows="4" cols="50" required></textarea><br>
            <button type="submit">Send</button>
        </form>
        <hr>
        <h2>Stored Messages</h2>
        <ul>
            {''.join(f'<li>{msg}</li>' for msg in messages)}
        </ul>
        <form method="post">
            <button type="submit" name="clear">Delete All Messages</button>
        </form>
    </body>
    </html>
    """

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    global messages
    if request.method == 'POST' and 'clear' in request.form:
        messages = []  # Clear all messages
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Admin Portal</title>
    </head>
    <body>
        <h1>Stored XSS Testing App</h1>
        <a href="/">Send Message</a> | <a href="/admin">Admin Portal</a>
        <hr>
        <h2>Admin Portal</h2>
        <ul>
            {''.join(f'<li>{msg}</li>' for msg in messages)}
        </ul>
        <form method="post">
            <button type="submit" name="clear">Delete All Messages</button>
        </form>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)

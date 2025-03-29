from flask import Flask, request, url_for, redirect, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/')
def home():
    return f'''
    <html>
    <head>
        <style>
            body {{ background-color: #f0f4f8; text-align: center; color: #333; font-family: 'Segoe UI', sans-serif; }}
            a {{ display: inline-block; margin: 10px; padding: 15px 30px; background-color: #4CAF50; text-decoration: none; color: white; border-radius: 8px; transition: background 0.3s; }}
            a:hover {{ background-color: #45a049; }}
            h1 {{ font-size: 3em; margin-bottom: 30px; }}
        </style>
    </head>
    <body>
        <h1>Welcome to the Homepage</h1>
        <a href="{url_for('profile')}">Go to Profile</a>
        <a href="{url_for('submit')}">Go to Submit Page</a>
    </body>
    </html>
    '''

@app.route('/profile')
def profile():
    name = session.get('name', 'Guest')
    age = session.get('age', 'Unknown')
    return f'''
    <html>
    <head>
        <style>
            body {{ background-color: #ffffff; text-align: center; color: #333; font-family: 'Segoe UI', sans-serif; }}
            a {{ background-color: #4CAF50; padding: 12px 24px; border-radius: 8px; color: white; text-decoration: none; }}
            a:hover {{ background-color: #45a049; }}
        </style>
    </head>
    <body>
        <h1>Profile Page</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Age:</strong> {age}</p>
        <a href="{url_for('home')}">Back to Homepage</a>
    </body>
    </html>
    '''

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        session['name'] = request.form.get('name', 'Unknown')
        session['age'] = request.form.get('age', 'Unknown')
        return redirect(url_for('profile'))
    
    return '''
    <html>
    <head>
        <style>
            body { background-color: #f0f4f8; text-align: center; color: #333; font-family: 'Segoe UI', sans-serif; }
            form { display: inline-block; background-color: #ffffff; padding: 30px; border-radius: 15px; box-shadow: 0 8px 16px rgba(0,0,0,0.1); }
            input { margin: 10px; padding: 12px; border-radius: 8px; border: 1px solid #ccc; width: 80%; }
            input[type="submit"] { background-color: #4CAF50; color: white; cursor: pointer; transition: background 0.3s; }
            input[type="submit"]:hover { background-color: #45a049; }
        </style>
    </head>
    <body>
        <h1>Submit Page</h1>
        <form method="post">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br>
            <label for="age">Age:</label>
            <input type="number" id="age" name="age" required><br>
            <input type="submit" value="Submit">
        </form>
        <a href="{url_for('home')}">Back to Homepage</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
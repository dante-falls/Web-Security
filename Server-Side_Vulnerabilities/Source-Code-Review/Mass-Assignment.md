<h1>Mass Assignment</h1>
A mass assignment vulnerability occurs when a web application automatically binds all user‑supplied input to internal object fields, allowing attackers to modify sensitive attributes such as roles, permissions, or admin flags 
without authorization.

<h2>The Vulnerable Code Snippet - Python Flask Application</h2>

```
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.secret_key = 'super_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(20), default='user')
    is_admin = db.Column(db.Boolean, default=False)

@app.route('/api/user/update', methods=['POST'])
def update_profile():
    # Ensure user is authenticated
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    user_id = session['user_id']
    incoming_data = request.get_json()
    
    if not incoming_data:
        return jsonify({"error": "No data provided"}), 400
        
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
        
    # Dynamically update user attributes based on incoming JSON payload
    for key, value in incoming_data.items():
        if hasattr(user, key):
            setattr(user, key, value)
            
    db.session.commit()
    
    return jsonify({
        "status": "success",
        "message": "Profile updated successfully",
        "user": {
            "username": user.username,
            "email": user.email,
            "bio": user.bio,
            "role": user.role,
            "is_admin": user.is_admin
        }
    })
```

<h2>The Issue</h2>

This is a classic Mass Assignment (or over-posting) vulnerability. Because the code loops through every key-value pair in the incoming JSON payload and blindly assigns them using setattr(user, key, value) 
for any attribute that exists on the model, an attacker can append sensitive fields like "role": "admin" or "is_admin": true to their JSON request. The application happily updates those internal database columns, instantly 
escalating the user's privileges.

<h2>The Fixed Code</h2>

```
from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.secret_key = 'super_secret_key'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(20), default='user')
    is_admin = db.Column(db.Boolean, default=False)

@app.route('/api/user/update', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
        
    user_id = session['user_id']
    incoming_data = request.get_json()
    
    if not incoming_data:
        return jsonify({"error": "No data provided"}), 400
        
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
        
    # Define an explicit allowlist of fields that users are permitted to modify
    ALLOWED_FIELDS = {'username', 'email', 'bio'}
    
    # Process only allowed fields, completely ignoring administrative attributes like role or is_admin
    for key, value in incoming_data.items():
        if key in ALLOWED_FIELDS:
            setattr(user, key, value)
            
    db.session.commit()
    
    return jsonify({
        "status": "success",
        "message": "Profile updated successfully",
        "user": {
            "username": user.username,
            "email": user.email,
            "bio": user.bio,
            "role": user.role,
            "is_admin": user.is_admin
        }
    })
```

By defining ALLOWED_FIELDS = {'username', 'email', 'bio'}, any attempt to inject is_admin or role in the JSON payload is ignored because those keys fail the "if key in ALLOWED_FIELDS" check

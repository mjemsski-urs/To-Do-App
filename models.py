from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash # For secure passwords

db = SQLAlchemy() # Create a SQLAlchemy database instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique user ID
    full_name = db.Column(db.String(100), nullable=False) # Full name
    email = db.Column(db.String(100), unique=True, nullable=False) # Email must be unique
    password_hash = db.Column(db.String(255), nullable=False) # Hashed password

    # A user can have many tasks
    tasks = db.relationship("Task", backref="user", lazy=True)

    # Hash the plain password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    # Verify password against the hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    # Convert user object to dictionary (for JSON/API use)
    def to_dict(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
        }

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique task ID
    title = db.Column(db.String(100), nullable=False) # Task description/title
    is_done = db.Column(db.Boolean, default=False) # Task status: done or not
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False) # Link to User

    # Convert task object to dictionary (for JSON/API use)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "is_done": self.is_done,
            "user_id": self.user_id,
        }

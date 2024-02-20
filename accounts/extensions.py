from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_mail import Mail
from flask_migrate import Migrate

# Create a Flask application instance
app = Flask(__name__)

# Initialize Flask extensions

# Bootstrap for styling client-side
bootstrap = Bootstrap4(app)

# CSRF protection for form submission
csrf = CSRFProtect(app)

# Set the SQLAlchemy database URI for MySQL
# Replace 'username', 'password', 'hostname', and 'database_name' with your MySQL credentials
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/flask_login'

# Disable SQLAlchemy track modifications to suppress a warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database for managing user data
database = SQLAlchemy(app)

# Login manager for managing user authentication
login_manager = LoginManager(app)

# Flask-Mail for sending email
mail = Mail(app)

# Flask-Migrate for database migrations
migrate = Migrate(app, database)

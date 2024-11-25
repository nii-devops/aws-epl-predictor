import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from authlib.integrations.flask_client import OAuth
from dotenv import load_dotenv
import awsgi
import boto3

from aws_lambda_wsgi import response
from werkzeug.middleware.proxy_fix import ProxyFix




def get_ssm_parameter(name):
    client = boto3.client('ssm')
    response = client.get_parameter(Name=name, WithDecryption=True)
    return response['Parameter']['Value']




# Load environment variables
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
oauth = OAuth()



def create_app():
    app = Flask(__name__, static_url_path='/https://nii-webapps.s3.us-east-1.amazonaws.com/epl-predictor/static/')
    #app.config.from_object('config.Config')

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    # Set the SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('AWS_DB_URI')#, 'sqlite:///site.db')  # Use environment variable or default to SQLite
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    
    # USING AWS SESSION MANAGER PARAMENTER STORE
    # app.config['SECRET_KEY'] = get_ssm_parameter('/myapp/SECRET_KEY')
    # app.config['SQLALCHEMY_DATABASE_URI'] = get_ssm_parameter('/myapp/DATABASE_URI')

    # Initialize extensions
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = 'login'

    Bootstrap5(app)

    # Apply middleware for AWS compatibility
    app.wsgi_app = ProxyFix(app.wsgi_app)
    # Register the `user_loader` function
    from .models import User

    oauth.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    # Import routes
    from app.routes import register_routes
    register_routes(app)

    with app.app_context():
        db.create_all()
        
    # # Lambda handler
    # def lambda_handler(event, context):
    #     return response(app, event, context)
    return app

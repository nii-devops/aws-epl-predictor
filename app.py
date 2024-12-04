import os
from app import app


# Create Flask app instance
#app = create_app()



# PRODUCTION ENVIRONMENT
if __name__ == '__main__':
    # Set the environment variable before running the app
    os.environ['FLASK_ENV'] = os.getenv('FLASK_ENV')
    app.run(debug=True)


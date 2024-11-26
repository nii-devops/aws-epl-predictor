
from app import create_app, db


# Create Flask app instance
app = create_app()


# PRODUCTION ENVIRONMENT
if __name__ == '__main__':
    app.run(debug=True)


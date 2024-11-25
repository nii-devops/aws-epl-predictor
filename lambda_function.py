from app import create_app, db
from aws_lambda_wsgi import response

# Create Flask app instance
app = create_app()

# Lambda handler function
def lambda_handler(event, context):
    """
    AWS Lambda entry point for Flask app.
    """
    app.run(host='0.0.0.0', port=8080)
    return response(app, event, context)


# PRODUCTION ENVIRONMENT
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Create tables if they don't exist
#     app.run(host='0.0.0.0', port=8080)


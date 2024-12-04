from app import app as application

def lambda_handler(event, context):
    return application(event, context)

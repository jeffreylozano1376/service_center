from app import app, db
from app.models import User, Service_Item

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Service_Item': Service_Item}
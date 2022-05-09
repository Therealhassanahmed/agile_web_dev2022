from app import app, db
from app.models import Location

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Location': Location}

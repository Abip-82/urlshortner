from flask import Flask
from dotenv import load_dotenv
import os
from db import db

load_dotenv() 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
db.init_app(app)

from views import views
app.register_blueprint(views , prefix='/')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug =True)
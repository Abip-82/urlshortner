from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv() 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

from views import views
app.register_blueprint(views , prefix='/')

if __name__ == '__main__':
    app.run()
from flask import Blueprint ,  render_template , request
from models import URL

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/shorten' , methods=["POST"])
def shorten():
    url =  request.form.get('url').strip()


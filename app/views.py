from app import app
from flask import render_template
from models import Category

@app.route('/')
def index():
	categories = Category.query.all()
	return render_template('index.html', categories=categories) 
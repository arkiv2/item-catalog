from app import app
from flask import render_template
from models import Category, Item

@app.route('/')
def index():
	categories = Category.query.all()
	items = Item.query.all()
	return render_template('index.html', categories=categories, items=items) 
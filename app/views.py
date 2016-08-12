from app import app
from flask import render_template
from models import Category, Item

@app.route('/')
def index():
	categories = Category.query.all()
	items = Item.query.all()
	return render_template('index.html', categories=categories, items=items) 

@app.route('category')
def category():
	categories = Category.query.all()
	return render_template('categories.html', categories=categories)

@app.route('category/<category_name>')
def category(category_name):
	category = Category.query.filter_by(slug_name=category_name).first_or_404()
	return render_template('category')

@app.route('item')
def item():
	categories = Category.query.all()
	items = Item.query.all()
	return render_template('items.html', categories=categories, items=items)

@app.route('item/<item_name>')
def item(item_name):
	item = Item.query.filter_by(slug_name=item_name).first_or_404()
	return render_template('item.html', )
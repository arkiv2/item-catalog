from app import app
from flask import render_template
from models import Category, Item

def include_sidebar_data(fn):
	template_name = fn()
	category_sidebar = Category.query.all()
	def wrapped():
		return render_template(template_name, category_sidebar=category_sidebar)
	return wrapped

@app.route('/')
@include_sidebar_data
def index():
	items = Item.query.all()
	return render_template('index.html', items=items) 

@app.route('category')
@include_sidebar_data
def category():
	categories = Category.query.all()
	return render_template('categories.html')

@app.route('category/<category_name>')
@include_sidebar_data
def category(category_name):
	category = Category.query.filter_by(slug_name=category_name).first_or_404()
	return render_template('category')

@app.route('item')
@include_sidebar_data
def item():
	items = Item.query.all()
	return render_template('items.html', items=items)

@app.route('item/<item_name>')
@include_sidebar_data
def item(item_name):
	item = Item.query.filter_by(slug_name=item_name).first_or_404()
	return render_template('item.html', )
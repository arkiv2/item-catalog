from app import db

class Category(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(180), index = True, unique = True)
	items = db.relationship("Item", db.back_populates = "category") 
class Item(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(180), nullable = False, index = True)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	category = db.relationship("Category", db.back_populates = "items")
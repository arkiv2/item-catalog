from app import db


class Category(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(180), index = True, unique = True)
	items = db.relationship('Item', back_populates = 'category') 

	def __repr__(self):
		return '<Category %r>' % self.name


class Item(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(180), nullable = False, index = True)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
	category = db.relationship('Category', back_populates = 'items')

	def __repr__(self):
		return '<Item %r>' % self.name
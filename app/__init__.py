from flask import Flask

app = Flask(__name__)
app.config.from_object('Config')
db = SQLAlchemy(app)

from app import views
from app import models

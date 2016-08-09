from app import app

@app.route('/')
def index():
	return "Welcome!"

	# return render_template('filename.html')  // TODO
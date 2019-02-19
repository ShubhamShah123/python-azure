# -*- coding: utf-8 -*-
# Librarys
from flask import Flask, render_template
import os
# Variables
app = Flask(__name__)

# Settings
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'secret'


# Views
@app.route('/', methods=('GET', 'POST'))
def index():
	return render_template('name.html')


# Run
if __name__ == '__main__':
	port = int(os.getenv('PORT', 8000))
	# app.run(host='0.0.0.0', port=port, debug=True)
	app.run(host='10.219.138.53', port=port, debug=True)

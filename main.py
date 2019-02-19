# -*- coding: utf-8 -*-
# Librarys
from flask import Flask, render_template, jsonify
import os
# Variables
app = Flask(__name__)

# Settings


# Views
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


# Run
if __name__ == '__main__':
	port = int(os.getenv('PORT', 8000))
	app.run(host='0.0.0.0', port=port, debug=True)
	# app.run(host='10.219.138.53', port=port, debug=True)

# -*- coding: utf-8 -*-
# Librarys
from flask import Flask, render_template, jsonify
import os
# Variables
app = Flask(__name__)

# Settings
app.config['DEBUG'] = True


# Views
@app.route('/', methods=['GET'])
def index():
	return jsonify({'status': 'Hello, World ! Running flask on Azure'}), 200


# Run
if __name__ == '__main__':
	port = int(os.getenv('PORT', 8000))
	# app.run(host='0.0.0.0', port=port, debug=True)
	app.run(host='10.219.138.53', port=port, debug=True)

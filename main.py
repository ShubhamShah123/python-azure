from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('index.html', name = "Shah Shubham", net_id = "sbs8554")

if __name__ == '__main__':
  port = int(os.getenv('PORT', 8000))
  app.run(host='0.0.0.0', port=port, debug=True)

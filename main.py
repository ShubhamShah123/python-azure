from imports import *
app = Flask(__name__)

DB_USERNAME = "shubhamshah"
DB_PASSWORD = "Shubh@mshah123"
CONNECTION_STRING = 'Driver={SQL Server};Server=tcp:sbssqlserver.database.windows.net,1433; Database=earthquakeDB; uid=shubhamshah@sbssqlserver;pwd=Shubh@mshah123'


def connect():
	connection = pdbc.connect()
	if connection:
		print("Success fully connected to the database")
	else:
		print("Connection failed")
	connection.close()

@app.route('/')
def hello_world():
  return render_template('index.html', name = "Shah Shubham !!", net_id = "sbs8554")


@app.route('/connect')
def connect_db():
	connect()
	return jsonify({'status': 'Connection'}), 200

if __name__ == '__main__':
  port = int(os.getenv('PORT', 8000))
  app.run(host='0.0.0.0', port=port, debug=True)

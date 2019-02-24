from imports import *
from flask.ext.mysql import MySQL

app = Flask(__name__)


DB_USERNAME = "shubhamshah"
DB_PASSWORD = "Shubh@mshah123"


mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'shubham123'
app.config['MYSQL_DATABASE_DB'] = 'dbtest'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def connect():
	print("Connect()")
	conn = mysql.connect()
	print("Con")
	if conn:
		print("CURSOR: YES\n")
		cursor = conn.cursor()
		if cursor:
			print("\tCURSOR: YES\n")
			return cursor
		else:
			print("\tCURSOR: NO\n")
			return 0
	else:
		print("CONN: NO")
		return 0

@app.route('/')
def hello_world():
  return render_template('index.html', name = "Shah Shubham", stud_id = "sbs8554")


@app.route('/connect', methods=['GET'])
def connect_db():
	print("-- connect db ---")
	con = connect()
	if con:
		con.execute('select * from data;')
		results = con.fetchall()
	else:
		pass
	return jsonify({'status':results}), 200

if __name__ == '__main__':
  port = int(os.getenv('PORT', 8000))
  app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DATABASE')

mysql = MySQL(app)

@app.route("/input")
def input():
    return render_template('input.html')
@app.route("/input", methods=['POST'])
def send():
    name = request.form['name']
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("INSERT INTO `table1` (`id`, `name`) VALUES (NULL, %s)", (name,))
    mysql.connection.commit()
    cursor.close()
    return render_template('input.html')

@app.route("/user")
def user():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM `table1`")
    users = cursor.fetchall()
    cursor.close()
    return render_template('user.html', users=users)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    if conn:
        conn.close()
from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'aaratech_db'

mysql = MySQL(app)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    cur = mysql.connection.cursor()

    cur.execute(
        """
        INSERT INTO leads (name, email, phone, message)
        VALUES (%s, %s, %s, %s)
        """,
        (name, email, phone, message)
    )

    mysql.connection.commit()
    cur.close()

    return """
    <h1>Thank You!</h1>
    <p>Your enquiry has been submitted successfully.</p>
    <a href="http://127.0.0.1:5500/contact.html">Go Back</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
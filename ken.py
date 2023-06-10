from flask import Flask, make_response, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config ["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "classicmodels"
# Extra configs, optional:
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)



@app.route("/customer", methods=["GET"])
def get_customer():
	cur = mysql.connection.cursor()
	query="""
    select * from customers
    """
	cur.execute(query)
	data = cur.fetchall()
	cur.close()
	return make_response(jsonify(data), 200)

@app.route("/customers/<int:customerNumber>", methods=["GET"])
def get_customer_by_number(customerNumber):
    cur = mysql.connection.cursor()
    query="""
    SELECT * FROM customers where customerNumber={}
    """.format(customerNumber)
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
	 
if __name__ == "__main__":
	app.run(debug=True)
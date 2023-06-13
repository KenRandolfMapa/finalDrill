from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "root"
app.config["MYSQL_DB"] = "classicmodels"
# Extra configs, optional:
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.ferchall()
    cur.close()

@app.route("/customer", methods=["GET"])
def get_customer():
    cur = mysql.connection.cursor()
    query = "SELECT * FROM customers"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return make_response(jsonify(data), 200)

@app.route("/customers/<int:customerNumber>", methods=["GET"])
def get_customer_by_number(customerNumber):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM customers WHERE customerNumber = %s"
    cur.execute(query, (customerNumber,))
    data = cur.fetchone()
    cur.close()
    return make_response(jsonify(data), 200)

@app.route("/employees", methods=["POST"])
def add_employees():
    cur = mysql.connection.cursor()
    info = request.get_json()
    firstName = info["firstName"]
    lastName = info["lastName"]
    cur.execute(
        "INSERT INTO employees (firstName, lastName) VALUES (%s, %s)",
        (firstName, lastName),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "employees added successfully", "rows_affected": rows_affected}
        ),
        201,
    )

@app.route("/employees/<int:employeeNumber>", methods=["PUT"])
def update_employees(employeeNumber):
    cur = mysql.connection.cursor()
    info = request.get_json()
    firstName = info["firstName"]
    lastName = info["lastName"]
    cur.execute(
        "UPDATE employees SET firstName = %s, lastName = %s WHERE employeeNumber = %s",
        (firstName, lastName, employeeNumber),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "actor updated successfully", "rows_affected": rows_affected}
        ),
        200,
    )

@app.route("/employees/<int:employeeNumber>", methods=["DELETE"])
def delete_employees(employeeNumber):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM employees WHERE employeeNumber = %s", (employeeNumber,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()
    return make_response(
        jsonify(
            {"message": "actor deleted successfully", "rows_affected": rows_affected}
        ),
        200,
    )

@app.route("/employees/format", methods=["GET"])
def get_params():
    fmt = request.args.get('employeeNumber')
    foo = request.args.get('aaaa')
    return make_response(jsonify({"format": fmt, "foo": foo}), 200)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, make_response
from flask import request


# using a new extension library to connect to mySQL
from flaskext.mysql import MySQL

# Creating the Flask app
app = Flask (__name__)
# Creating an instance of the Flask object and 
# it is providing us the base name of this module

app.config['MYSQL_DATABASE_HOST'] = 'db_server'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'webapp'
app.config['MYSQL_DATABASE_PASSWORD'] = 'tbtDatabase3200'
app.config['MYSQL_DATABASE_DB'] = 'trainbt'

db_conn = MySQL()
# initialize everything
db_conn.init_app(app)

# Passenger Wireframe #1:
# passenger gives feedback to a particular specific train car
@app.route('/add_feedback', methods = ['POST'])
def give_feedback():
    app.logger.info(request.form)
    comment = request.form['comment']
    trainid = request.form['trainid']
    rating = request.form['rating']
    query = f'INSERT INTO feedback(comment, trainid, rating) VALUES(\"{comment}\", \"{trainid}\", \"{rating}\")'
    cursor = db_conn.get_db().cursor()
    cursor.execute(query)
    db_conn.get_db().commit()
    cursor.connection.commit()
    return "Success!" 

# Passenger Wireframe #2: 
# display the current balance of a passenger's train card
@app.route('/card_funds')
def current_funds():
    query = f'SELECT currentBalance from trainCard WHERE trainCard.pID = passengers.passengerID'
    cur = db_conn.get_db().cursor()
    cur.execute(query)
    funds = []
    funds_data = cur.fetchall()
    for row in funds_data:
        funds.append(row[0])
    return jsonify(funds[0])

# Conductor Wireframe #1:
# update the schedule with which route and stop
# the conductor is late to and by how much time
@app.route('/update_delay', methods = ['POST'])
def add_delay():
    app.logger.info(request.form)
    trainid = request.form['trainid']
    routeid = request.form['routeid']
    stopid = request.form['stopid']
    delayAmt = request.form['delayAmt']
    query = f'INSERT INTO delays(trainid, routeid, stopid, delayAmt) VALUES(\"{trainid}\", \"{routeid}\", \"{stopid}\", \"{delayAmt}\")'
    cursor = db_conn.get_db().cursor()
    cursor.execute(query)
    db_conn.get_db().commit()
    cursor.connection.commit()
    return "Success!" 

# Conductor Wirefrarme #2:
# display the feedback that a conductor has received
# feedback is anonymized when viewed on the website
@app.route('/feedback')
def get_feedback():
    condID = request.args.get('condID', default = 0, type = int)
    cur = db_conn.get_db().cursor()
    cur.execute(f'select * from feedback where condID={condID}')
    col_headers = [x[0] for x in cur.description]
    json_data = []
    the_data = cur.fetchall()
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)

# Manager Wireframe #1: Keep track of a given conductor's rating, start date, and feedback history.
@app.route('/cdtr_rating_history')
def get_rating_history():
    condID = request.args.get('condID', default = 0, type = int)
    cur = db_conn.get_db().cursor()

    cur.execute(f'select * from feedback where condID={condID}')
    col_headers = [x[0] for x in cur.description]
    feedback = []
    the_data = cur.fetchall()
    for row in the_data:
        feedback.append(dict(zip(col_headers, row)))

    cur.execute(f'select AVG(rating) from feedback where condID={condID}')
    rating = []
    rating_data = cur.fetchall()
    for row in rating_data:
        rating.append(row[0])

    cur.execute(f'select startDate from conductors where conductorID={condID}')
    start_date = []
    start_date_data = cur.fetchall()
    for row in start_date_data:
        start_date.append(row[0])

    return jsonify({
        "feedback": feedback,
        "rating": rating[0],
        "start_date": start_date[0]})

# Manager Wireframe #2:
# create a new train schedule
@app.route('/new_sched', methods = ['POST'])
def create_schedule():
    app.logger.info(request.form)
    routeid = request.form['routeid']
    stopid = request.form['stopid']
    query = f'INSERT INTO delays(trainid, routeid, stopid, delayAmt) VALUES(\"{routeid}\", \"{stopid}\")'
    cursor = db_conn.get_db().cursor()
    cursor.execute(query)
    db_conn.get_db().commit()
    cursor.connection.commit()
    return "Success!" 

# get the history of transactions on a passenger's train card
@app.route('/tcard_history')
def tcard_history():
    passID = request.args.get('passID', default = 0, type = int)
    cur = db_conn.get_db().cursor()
    cur.execute(f'select * from transactions where pID={passID}')
    col_headers = [x[0] for x in cur.description]
    json_data = []
    the_data = cur.fetchall() 
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)

# get all the passengers in the database
@app.route('/all_passengers')
def get_passengers():
    cur = db_conn.get_db().cursor()
    cur.execute('select * from passengers')
    col_headers = [x[0] for x in cur.description]
    json_data = []
    the_data = cur.fetchall() 
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)

# get all the trains in the database
@app.route('/all_trains')
def get_trains():
    cur = db_conn.get_db().cursor()
    cur.execute('select * from train')
    col_headers = [x[0] for x in cur.description]
    json_data = []
    the_data = cur.fetchall() 
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)

# get all the conductors in the database
@app.route('/all_conductors')
def get_conductors():
    cur = db_conn.get_db().cursor()
    cur.execute('select * from conductors')
    col_headers = [x[0] for x in cur.description]
    json_data = []
    the_data = cur.fetchall() 
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)

# get all the managers in the database
@app.route('/all_managers')
def get_managers():
    cur = db_conn.get_db().cursor()
    cur.execute('select * from managers')
    col_headers = [x[0] for x in cur.description]
    json_data = []
    the_data = cur.fetchall() 
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)



# get all the feedback categories
@app.route('/all_categ')
def get_categories():
    cur = db_conn.get_db().cursor()
    cur.execute('select category from feedback')
    col_headers = [x[0] for x in cur.description]
    json_data = []
    the_data = cur.fetchall() 
    for row in the_data:
        json_data.append(dict(zip(col_headers, row)))
    return jsonify(json_data)


# Allows the file to run independently 
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 4000)

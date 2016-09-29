from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '53curity'
app.config['MYSQL_DATABASE_DB'] = 'BucketList'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')


@app.route('/showSignIn')
def showSignIn():
    return render_template('signin.html')


@app.route('/signUp', methods=['POST'])
def signUp():

    # read the posted values from the UI
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # # validate the received values
    # if _name and _email and _password:
    #     return json.dumps({'html':'<span>All fields good !!</span>'})
    # else:
    #     return json.dumps({'html':'<span>Enter the required fields</span>'})

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_createUser', (_name, _email, _password))
    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        return json.dumps({'message': 'User created successfully !'})
    else:
        return json.dumps({'error': str(data[0])})


if __name__=="__main__":
    app.run()


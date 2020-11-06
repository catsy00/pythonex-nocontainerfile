import os
from flask import Flask
import pymysql
app = Flask(__name__)

@app.route("/")
def main():
    color = os.environ.get('COLOR', "green") 
    message = "Welcome !!! This is "+color+" environment  TJKIM" 
    return message

@app.route('/db')
def db_select():

    try: 
        db = pymysql.connect(host='mysql-pv',port=3306, user='root',passwd='minkim', db='sampledb',charset='utf8',autocommit=True)

        cursor = db.cursor()
        cursor.execute("SELECT * FROM sampledb;")
        data = cursor.fetchone()
        return data
    finally:
        if con:
            con.close()

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/egg')
def egg():
    return "hot!!!!"

@app.route('/healthz')
def healthz():
    return "OK!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
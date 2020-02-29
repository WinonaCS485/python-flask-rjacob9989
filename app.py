from flask import Flask, render_template
import pymysql.cursors
#import json
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)


@app.route('/dbtest')
def dbtest():

    # Connect to the database
    connection = pymysql.connect(host='mrbartucz.com',
                                user='av6352tk',
                                password='Buddha414!',
                                db='av6352tk_University',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
         # Select all Students
         #key = input("Enter a name to search:\n" )
         sql = """SELECT * from Students"""
         # WHERE Name LIKE %s"""
        
         # execute the SQL command
         cursor.execute(sql)
         
        t1 = []
        #s_result = ''
        for result in cursor:
            t1.append(result)
            #s_result += "\n" + str(result)
            print (result)

      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

    finally:
        connection.close()

    #return render_template('db_test.html', result )
    return render_template('db_test.html', result=t1)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6352)